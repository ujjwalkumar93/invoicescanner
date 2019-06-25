from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string
import re
pages = convert_from_path('Invoice.pdf', 500)

for page in pages:
    newimg=page.resize((2000,2000))
    newimg.save('mungi.png', 'PNG')
    #pageimg=page.save('saved.jpg','JPEG')
    #print(pageimg)
image = Image.open('mungi.png', mode='r')
print(image_to_string(image))
#mylist=[image_to_string(image).split()]

#print(mylist)
print("index is:  ")
