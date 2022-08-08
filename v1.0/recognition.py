from paddleocr import PaddleOCR, draw_ocr
import re
import os
os.environ['KMP_DUPLICATE_LIB_OK']='True'


def process(result):
    number = None
    valid_thru = None

    for line in result:
        #модель иногда путает цифру 1 c английской буквой l и цифру 6 с буковой b (в некоторых шрифтах), поэтому заменяем
        buf = re.sub('l', '1', line[1][0])
        buf = re.sub('b', '6', buf)
        #срок действия карты всегда идет после номера, поэтому до того как нашли номер искать срок нет смысла
        #также это исключает обнаружение срока действия в поле с номером (в поле с номером срока действия точно нет)
        if(number is None): 
            #извлекаем цифры из поля
            buf = re.findall('[0-9]', buf)
            if(len(buf) == 16):
                number = buf
        else:
            buf = re.findall('[0-9]{2}/[0-9]{2}', line[1][0])
            if(len(buf) != 0):
                valid_thru = buf[-1]
                break
                
    return number, valid_thru
                

def scan(img_path, model, debug=False):
    result = model.ocr(img_path, cls=True)
    
    if(debug):
        print([el[1:] for el in result])
    
    num, valid_thru = process(result)
    
    if(num is not None):
        num = ''.join(num)
    
    return num, valid_thru
    

def test(img_root, test_size, model):
    preds = list()

    for i in range(test_size):
        preds.append(scan(img_root + f'image_{i}.jpg', model))
    
    return preds

