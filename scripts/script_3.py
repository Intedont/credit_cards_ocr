
'''
Заменяет знак разделения \t на пробел
'''

path_from = 'projects\\credit_cards_ocr\\datasets\\cropped\\generated_2\\labels.txt'
path_to = 'projects\\credit_cards_ocr\\datasets\\cropped\\generated_2\\mmocr_train.txt'

with open(path_to, 'w') as ff:
    pass

with open( path_from, 'r') as f:
    lines = f.readlines()
    for line in lines:
        with open(path_to, 'a') as ff:
            new_line = line.replace('\t', ' ')
            ff.write(new_line)
