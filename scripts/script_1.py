
'''
разделяет номера карт пробелами
'''

path_from = 'projects\\credit_cards_ocr\\datasets\\cropped\\generated_2\\labels.txt'
path_to = 'projects\\credit_cards_ocr\\datasets\\cropped\\generated_2\\withspaces.txt'

with open(path_to, 'w') as ff:
    pass

with open( path_from, 'r') as f:
    lines = f.readlines()
    for line in lines:
        with open(path_to, 'a') as ff:
            delimiter_idx = line.find('\t')
            new_line = line[:delimiter_idx + 5] + ' ' + line[delimiter_idx + 5 : delimiter_idx + 9] + ' ' + line[delimiter_idx + 9 : delimiter_idx + 13] + ' ' + line[delimiter_idx + 13:]
            print(new_line)
            ff.write(new_line)
