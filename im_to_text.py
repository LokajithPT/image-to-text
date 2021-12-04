import pytesseract as tess
tess.pytesseract.tesseract_cmd = r'F:\\VS code\\image to text\\tesseract.exe' #this path is my directory to tesseract
from PIL import Image
def main():
    print("make sure that there are no ' or & ")
    usr = input("drag and drop the img file here:")
    img = Image.open(usr)
    text = tess.image_to_string(img)
    print(text)
    main()
    
main()
