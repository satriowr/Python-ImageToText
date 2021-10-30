import cv2
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' #your tesseract path


img = cv2.imread('') #Your Image

def string(img) :
    text = pytesseract.image_to_string(img)
    return text


print(string(img))
