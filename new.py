from qrtools import QR 
import os
# creates the QR object 
my_QR = QR(data = u"Example") 
  
# encodes to a QR code 
my_QR.encode() 
os.rename(my_QR.filename,'new1.png') 
os.system("sudo mv " + 'new1.png' + " ~/pdf_to_text") 

print(my_QR.filename)

