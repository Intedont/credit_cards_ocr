from PIL import Image
import os

Image.MAX_IMAGE_PIXELS = 29041593885 


def crop_from_yolo(images_path, boxes_path, save_path):
    '''Создает датасет для обучения модели распознавания

    Args:
        images_path: путь к папке с исходными изображениями
        boxes_path: путь к папке с размеченными боксами (в формате yolo датасета)
        save_path: путь к папке, куда сохранять обрезанные изображения
    '''
    for filename in os.listdir(images_path):
        print(f'processing {filename}')
        img = Image.open(images_path + '\\' + filename)
        line = []
        with open(boxes_path + '\\' + filename[:-3] + 'txt', 'r') as f:
            line = f.read().split()
        
        line = [float(x) for x in line]
        w, h = img.size

        left = round((line[1] - line[3]/2) * w)
        right = round(left + line[3] * w)
        upper = round((line[2] - line[4]/2) * h)
        lower = round(upper + line[4] * h)

        box = (left, upper, right, lower)
        img2 = img.crop(box)

        if(img2.mode != 'RGB'):
            img2 = img2.convert('RGB')

        img2.save(save_path + '\\' + filename)

crop_from_yolo('projects\\credit_cards_ocr\\datasets\\yolo\\images\\val',
            'projects\\credit_cards_ocr\\datasets\\yolo\\labels\\val',
            'projects\\credit_cards_ocr\\datasets\\cropped\\val')
