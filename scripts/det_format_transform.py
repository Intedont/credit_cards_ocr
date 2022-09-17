import os
import xml.etree.ElementTree as ET


path_labels = 'projects\\credit_cards_ocr\\v2_0\\PaddleOCR\\train_data\\labels_val\\'
path_to = 'projects\\credit_cards_ocr\\v2_0\\PaddleOCR\\train_data\\'


for filename in os.listdir(path_labels):
    print(filename)
    tree = ET.parse(path_labels + filename)
    root = tree.getroot() 
    xmin = int(root[6][4][0].text)
    ymin = int(root[6][4][1].text)
    xmax = int(root[6][4][2].text)
    ymax = int(root[6][4][3].text)
    print(xmin, ymin, xmax, ymax)

    to_write = '[{"transcription": "", "points": ' + f'[[{xmin}, {ymin}], [{xmax}, {ymin}], [{xmax}, {ymax}], [{xmin}, {ymax}]]' + '}]'

    
    with open(path_to + 'labels.txt', "a") as f:
        text = f.write(filename[:-3] + 'jpg' + '\t' + str(to_write) + '\n')
