# Import libraries
from google.colab import files
import pytesseract
import easyocr
import cv2
from google.colab.patches import cv2_imshow

# Define the OCR reader
reader = easyocr.Reader(['en'])

# Define functions
def get_num(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2_imshow(image)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    text = pytesseract.image_to_string(thresh, config='outputbase digits')
    print("Text extracted using pytesseract:", text)

def get_num_easyocr(path):
    image = cv2.imread(path, cv2.IMREAD_GRAYSCALE)
    cv2_imshow(image)
    thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY | cv2.THRESH_OTSU)[1]
    result = reader.readtext(thresh)
    text = ' '.join([res[1] for res in result])
    print("Text extracted using EasyOCR:", text)

# Prompt user to upload a file
uploaded = files.upload()

# Process uploaded files
for file_name in uploaded.keys():
    print(f"Processing file: {file_name}")
    get_num(file_name)
    get_num_easyocr(file_name)
