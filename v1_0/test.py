from recognition import test, scan
from paddleocr import PaddleOCR

ocr = PaddleOCR(use_angle_cls=True, lang='en')

pred = scan('../images/image_1.jpg', ocr)
print(pred)

test_preds = test('../images/', 8, ocr)
print(test_preds)

pred = scan('../images/image_1.jpg', ocr, return_coords=True)
print(pred)
