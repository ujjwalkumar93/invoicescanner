import re
import xlwt
from xlwt import Workbook

# Open the file for reading
with open('new_text.txt','r+') as fd:

    # Iterate over the lines
    i=0
    for line in fd:
    	
    	# Capture one-or-more characters of non-whitespace after the initial match
        vendor_code_s = re.search(r'Vendor Code (\S+)', line)
        invoice_no_s=re.search(r'Invoice Number (\S+)', line)
        invoice_date_s=re.search(r'Invoice Date (\S+)', line)
        gsin_vendor_s=re.search(r'GSTIN Number (\S+)', line)
        gstin_bill_party_s=re.search('GSTIN :', line)
        hsn_sac_s=re.search(r'HSN (\S+)', line)
        place_supply_s=re.search(r'Place of Supply (\S+)', line)
        total_invoice_s=re.search(r'TOTAL INVOICE VALUE (\S+)', line)
        cgst_s=re.search('CGST', line)
        sgst_s=re.search('SGST', line)
        if vendor_code_s:
        	list_of_words = line.split()
        	vendor_code= list_of_words[list_of_words.index("Code")+2]
        	print(vendor_code)
        if invoice_no_s:
        	list_of_words = line.split()
        	invoice_no= list_of_words[list_of_words.index("Number")+2]
        	print(invoice_no)
        if invoice_date_s:
        	list_of_words = line.split()
        	invoice_date= list_of_words[list_of_words.index("Date")+2]
        	print(invoice_date)	
        if gsin_vendor_s:
        	list_of_words = line.split()
        	gsin_vendor= list_of_words[list_of_words.index("Number")+2]
        	print(gsin_vendor)	
        if gstin_bill_party_s:
        	list_of_words = line.split()
        	gstin_bill= list_of_words[list_of_words.index(":")+1]
        	gstin_ship=list_of_words[list_of_words.index(":")+4]
        	print(gstin_bill)	
        	print(gstin_ship)
        if hsn_sac_s:
        	list_of_words = line.split()
        	hsn_sac= list_of_words[list_of_words.index("HSN")+6]
        	print(hsn_sac)	
        if place_supply_s:
        	list_of_words = line.split()
        	place_supply= list_of_words[list_of_words.index("Supply")+2]
        	print(place_supply)		
        # if total_invoice_s:
        # 	list_of_words = line.split()
        # 	i=len(list_of_words)
        # 	test=""
        # 	for d in range(i):
        # 		test= list_of_words[list_of_words.index("INVOICE"):d]
        # 		test=test+" "
        # 	print(test)
        if cgst_s:
        	list_of_words = line.split()
        	cgst= list_of_words[list_of_words.index("@")+1]
        	print(cgst)
        if sgst_s:
        	list_of_words = line.split()
        	sgst= list_of_words[list_of_words.index("@")+1]
        	cgst_sgst=cgst+","+sgst
        	print(sgst)
        	print(cgst_sgst)
        #print(type(fd))
        #str(fd,'utf-8')
        #test=fd.find('Vendor Code :')
    	# Did we find a match?
        # if match:
        #     # Yes, process it
        #     weather = match.group(1)
        #     print('Vendor Code: {}'.format(weather))
        #     break
        # else :
        # 	print("")
        	
            

wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0, "Vendor Code")
sheet1.write(0,1, vendor_code)
sheet1.write(1,0, "Vendor Name & Address")
sheet1.write(2,0, "GSTIN of Vendor")
sheet1.write(2,1, gsin_vendor)
sheet1.write(3,0, "Name of State and State Code")
sheet1.write(4,0, "Invoice No.")
sheet1.write(4,1, invoice_no)
sheet1.write(5,0, "Invoice date")
sheet1.write(5,1, invoice_date)
sheet1.write(6,0, "TML Po No")
sheet1.write(7,0, "Ship-to-Party Name & Address")
sheet1.write(8,0, "GSTIN of Bill-to-Party ( TML )")
sheet1.write(8,1, gstin_bill)
sheet1.write(9,0, "Name & address of  Bill-to-Party ( TML )")
sheet1.write(10,0, "GSTIN of Ship-to-Party")
sheet1.write(10,1, gstin_ship)
sheet1.write(11,0, "HSN / SAC code")
sheet1.write(11,1, hsn_sac)
sheet1.write(12,0, "Place of Supply")
sheet1.write(12,1, place_supply)
sheet1.write(13,0, "TML Part No")
sheet1.write(14,0, "Description of goods or services")
sheet1.write(15,0, "Qty.  & its Unit of Measurement)")
sheet1.write(16,0, "Rate / Unit")
sheet1.write(17,0, "Total Taxable value")
sheet1.write(18,0, "Appicable Rate of tax (CGST, SGST(UTGST)/IGST/CESS)")
sheet1.write(18,1, cgst_sgst)
sheet1.write(19,0, "Amount of tax")
sheet1.write(20,0, "Total Invoice value")


wb.save('xlwt exampleTest.xls')



