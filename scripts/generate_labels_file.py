import os
from re import I
from PIL import Image

path_from = 'projects\\ocr_generator\\TextRecognitionDataGenerator\\out'
path_to = 'projects\\credit_cards_ocr\\images'
labels_path = 'labels.txt'

with open(labels_path, 'w'):
    pass

i = 300
for filename in os.listdir(path_from):
    
    img = Image.open(path_from + '\\' + filename)
    img.save(path_to + '\\' + f'image_{i}.jpg')

    with open(labels_path, 'a') as f:
        f.write(f'train/image_{i}.jpg\t' + filename[:22].replace(' ', '') + '\n')
    i += 1