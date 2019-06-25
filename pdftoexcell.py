from pdf2image import convert_from_path
from PIL import Image
from pytesseract import image_to_string
import xlwt
from xlwt import Workbook

pages = convert_from_path('Invoice.pdf', 500)

for page in pages:
    newimg=page.resize((2000,2000))
    newimg.save('mungi.png', 'PNG')
    #pageimg=page.save('saved.jpg','JPEG')
    #print(pageimg)
image = Image.open('mungi.png', mode='r')
#print(image_to_string(image))
mylist=image_to_string(image)
str=mylist.split()[1]

data={
    "vendor_code": "",
    "vendor_name_address":"Null",
    "gst_vendor":"Null",
    "state_code":"Null",

}
data['vendor_code']+=''.join(mylist)


print(str)
print("data is: ",data)
print(mylist)

#code for excell
wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0, "Vendor Code")
sheet1.write(1,0, "Vendor Name & Address")
sheet1.write(2,0, "GSTIN of Vendor")
sheet1.write(3,0, "Name of State and State Code")
sheet1.write(4,0, "Invoice No.")
sheet1.write(5,0, "Invoice date")
sheet1.write(6,0, "TML Po No")
sheet1.write(7,0, "Ship-to-Party Name & Address")
sheet1.write(8,0, "GSTIN of Bill-to-Party ( TML )")
sheet1.write(9,0, "Name & address of  Bill-to-Party ( TML )")
sheet1.write(10,0, "GSTIN of Ship-to-Party")
sheet1.write(11,0, "HSN / SAC code")
sheet1.write(12,0, "Place of Supply")
sheet1.write(13,0, "TML Part No")
sheet1.write(14,0, "Description of goods or services")
sheet1.write(15,0, "Qty.  & its Unit of Measurement)")
sheet1.write(16,0, "Rate / Unit")
sheet1.write(17,0, "Total Taxable value")
sheet1.write(18,0, "Appicable Rate of tax (CGST, SGST(UTGST)/IGST/CESS)")
sheet1.write(19,0, "Amount of tax")
sheet1.write(20,0, "Total Invoice value")


wb.save('xlwt exampleTest.xls')

