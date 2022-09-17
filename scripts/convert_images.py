from PIL import Image
import os

path = 'projects\\ocr_generator\\TextRecognitionDataGenerator\\out\\'
path_to = 'projects\\credit_cards_ocr\\images'

i = 0
for filename in os.listdir(path):
    print(path + filename)
    im1 = Image.open(path + filename).convert('RGB')
    im1.save(path_to + f'image_{i}.jpg')
    i += 1

