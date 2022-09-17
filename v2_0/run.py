import os
os.environ['KMP_DUPLICATE_LIB_OK']='TRUE'
import torch
from PIL import Image
from paddleocr import PaddleOCR
import numpy
from mmocr.utils.ocr import MMOCR


class RecModel():
    '''Класс обертка над моделями

    Реализует единый интерфейс для моделей разных типов
    '''
    def __init__(self, type, path_model, path_dict=None, path_config=None, image_reshape=[3, 32, 400], ocr_version='PP-OCRv2'):
        '''
        Args:
            type: тип модели (paddleocr или mmocr)
            path_model: путь к файлу модели
            path_dict: путь к файлу со словарем распознаваемых символов (только для paddleocr)
            path_config: путь к файлу с конфигом модели (только для mmocr)
            image_reshape: размер изображения, на котором обучалась модель paddleocr
            ocr_version: версия paddleocr (paddleocr не дает установить кастомный размер изображения, 
                         а у OCRv2 размер наиболее близок к использованному для тренировки) 
        '''
        self.type = type
        if(type == 'paddleocr'):
            self.model = PaddleOCR(det=False, cls=False, ocr_version=ocr_version,  rec_image_shape=image_reshape, rec_model_dir=path_model, rec_char_dict_path=path_dict)
        elif(type == 'mmocr'):
            print(path_config)
            self.model = MMOCR(det=None, recog_config=path_config, recog_ckpt=path_model)
        else: raise ValueError(f'Incorrect model type. Model supports "paddleocr" and "mmocr" but you pass "{type}"')

    def predict(self, img):
        if(self.type == 'paddleocr'):
            ans = self.model.ocr(numpy.array(img), det=False, cls=False)
            return ans[0][0]
        else:
            ans = self.model.readtext(numpy.array(img))
            return ans[0]['text']


class CardsOcr():
    '''Главный класс ocr модуля
    '''
    def __init__(self, rec_type, path_det, path_rec, path_dict=None, path_config=None, path_yolo='./yolov5') -> None:
        '''
        Args:
            rec_type: тип recognition модели
            path_det: путь к yolo модели
            path_rec: путь к recognition модели
            path_dict: путь к словарю распознаваемых символов (только при rec_type='paddleocr')
            path_config: путь к конфигу модели (только при rec_type='mmocr')
            path_yolo: путь к установленному репозиторию с yolov5 (нужно для локальной инициализации модели)
        '''
        self.det_model = torch.hub.load(path_yolo, 'custom', path=path_det, source='local')
        self.rec_model = RecModel(rec_type, path_rec, path_dict=path_dict, path_config=path_config)

    def predict(self, img_path):
        '''Сканирует картинку и возвращает найденный номер карты
        Если yolo не задетектил номер - возвращает None
        Args:
            img_path: путь к изображению
        '''
        img = Image.open(img_path)
        img1 = self.detect(img)

        if(img1 != None):
            ans = self.rec_model.predict(img1)
            return ans
        else: return None

    def detect(self, img):
        '''Выполняет детекцию номера при помощи yolo модели
        Вырезает найденную область и возвращает ее в формате PIL Image
        '''
        res = self.det_model(img)

        if(res.pred[0].shape[0] != 0):
            
            res_max = res.xyxy[0][:,4].argmax()
            left = res.xyxy[0][res_max][0].item()
            top = res.xyxy[0][res_max][1].item()
            right = res.xyxy[0][res_max][2].item()
            bottom = res.xyxy[0][res_max][3].item()
            
            img1 = img.crop((left, top, right, bottom))
            #img1 = img1.resize((400, 32))
            #img1.show()

            return img1

        else: return None
    

if __name__ == '__main__':
    ocr = CardsOcr('paddleocr', './models/yolo/best.pt', './models/paddle/model', path_dict='./models/paddle/word_dict.txt')
    #ocr = CardsOcr('mmocr', './models/yolo/best.pt', './models/mmocr/satrn_0.92.pth', path_config='./models/mmocr/configs/satrn_academic.py')
    ans = ocr.predict('../datasets/yolo/images/val/image_10.jpg')
    print(ans)
