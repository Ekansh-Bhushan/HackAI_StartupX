import pytesseract as tess
from PIL import Image

img=Image.open('image.jpeg')
text=tess.image_to_string(img)


if __name__ == "__main__":
    print(text)