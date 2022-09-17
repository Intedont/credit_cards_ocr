from v1_0.recognition import scan
import os
from paddleocr import PaddleOCR

'''Скрипт для автоматической разметки датасета для модели детекции'''

images_root = 'projects\\credit_cards_ocr\\v2_0\\PaddleOCR\\train_data\\images_proc\\'
labels_path = 'projects\\credit_cards_ocr\\v2_0\\PaddleOCR\\train_data\\labels.txt'
model = PaddleOCR(use_angle_cls=True, lang='en')
file = open(labels_path, 'w')
not_recognized = []

for filename in os.listdir(images_root):
    print(filename)
    pred = scan(images_root + filename, model, return_coords=True)
    print(pred)
    try:
        to_write = [{"transcription": pred[0][0], "points":pred[0][1]}]
        if(pred[1] is not None):
            to_write.append({"transcription": pred[1][0], "points":pred[1][1]})
        file.write(filename + ' ' + to_write)
        #with open(labels_path, "w") as f:
        #    text = f.write(filename + ' ' + to_write)
    except TypeError:
        not_recognized.append(filename)

print(f'not_recognized: {not_recognized}')
file.close()
