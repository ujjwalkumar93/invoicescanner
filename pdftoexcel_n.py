import re
import xlwt
from xlwt import Workbook
import datetime
import os
from itertools import islice
# Open the file for reading
#file_name="new_test.txt"
#os.chmod(file_name, 777)
#os.system('sudo su')
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
        total_taxable_s=re.search(r'TOTAL GST (\S+)', line)
        cgst_s=re.search('CGST', line)
        sgst_s=re.search('SGST', line)
        qty=re.search('Qty Unit ', line)

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
        if total_invoice_s:
            list_of_words = line.split()
            i=len(list_of_words)-6
            print(i)
            print("SEE ABOVE")
            total_invoice_f=""
            for d in range(i):
                test= list_of_words[list_of_words.index(":")+d]
                if test!= ":" :
                    total_invoice_f+=test+" "
            print(total_invoice_f)
            print("SEE ABOVE NOW")

        if total_taxable_s:
            list_of_words = line.split()
            i=len(list_of_words)-6
            print(i)
            print("SEE ABOVE")
            total_taxable_f=""
            for d in range(i):
                test= list_of_words[list_of_words.index("Rs.")+d]
                if test!= "Rs." :
                    total_taxable_f+=test+" "
            print(total_taxable_f)
            print("SEE ABOVE NOW")

        if qty:
            list_of_words=line.split()
            print(list_of_words)
            print("Quantity above")

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
with open('new_text.txt','r+') as myfile:
	for l in myfile:
		tml_poa_s=re.search(r'L.R. No (\s+)',l)
		ship_to_party_s=re.search(r'(Shipped to Address of delivery) (\s+)',l)
		state_code_s=re.search(r'MAHARASHTRA',l)
		part_no_s=re.search(r'1  (\s+)' or r'2 (\s+)' or r'3 (\s+)'or r'4 (\s+)'or r'5 (\s+)'or r'6 (\s+)',l)
		total_invoice_s=re.search(r'INVOICE TOTAL ',l)

		if tml_poa_s:
			words=l.split()
			tml_po=words[words.index("No")+2]
			print(tml_po)
		else:
			tml_po="NA"
		if ship_to_party_s:
			words=l.split()
			ship_to_party=words[words.index("TATA MOTORS LIMITED")+10]
			#print(ship_to_party)
		if total_invoice_s:
			words=l.split()
			total_invoice=words[words.index("Rs.")+1]
			print(total_invoice)
		if state_code_s:
			words=l.split()
			state_code=words[words.index("MAHARASHTRA" or "TAMILNADU" or "GUJRAAT" or "KERALA")+1]
			print(state_code)
		if state_code_s:
			words=l.split()
			state=words[words.index("MAHARASHTRA" or "TAMILNADU" or "GUJRAAT" or "KERALA")+0]
			#print(state+" "+state_code)
		if part_no_s:
			words=l.split()
			#mlist=[words][1,4]
			#part_no=words[words.index("1" )+2]
			print(words)

complete_state=state+" "+state_code
print(complete_state)

with open('new_text.txt') as f:
    for line in f:
        if '(Shipped to Address of delivery)' in line:
			#name_add=''.join(islice(f, 4))
            name_add=''.join(islice(f, 4))


with open('new_text.txt','r+') as mfile:
	for vendor in islice(mfile,1,2):
		#str=line.replace("\r", "\t")
		#vendor_name=vendor
		#print(vendor_name)
		if vendor:
			vendor_name=vendor
			#print(vendor_name)
		for adress in islice(mfile,1):
			vendor_add=adress
			complete_vendor=vendor_name+vendor_add
			print(complete_vendor.strip())

wb = Workbook()

# add_sheet is used to create sheet.
sheet1 = wb.add_sheet('Sheet 1')
sheet1.write(0,0, "Vendor Code")
sheet1.write(0,1, vendor_code)
sheet1.write(1,0, "Vendor Name & Address")
sheet1.write(1,1, complete_vendor)
sheet1.write(2,0, "GSTIN of Vendor")
sheet1.write(2,1, gsin_vendor)
sheet1.write(3,0, "Name of State and State Code")
sheet1.write(3,1,complete_state)
sheet1.write(4,0, "Invoice No.")
sheet1.write(4,1, invoice_no)
sheet1.write(5,0, "Invoice date")
sheet1.write(5,1, invoice_date)
sheet1.write(6,0, "TML Po No")
sheet1.write(6,1, tml_po)
sheet1.write(7,0, "Ship-to-Party Name & Address")
sheet1.write(7,1, name_add)
sheet1.write(8,0, "GSTIN of Bill-to-Party ( TML )")
sheet1.write(8,1, gstin_bill)
sheet1.write(9,0, "Name & address of  Bill-to-Party ( TML )")
sheet1.write(9,1, name_add)
sheet1.write(10,0, "GSTIN of Ship-to-Party")
sheet1.write(10,1, gstin_ship)
sheet1.write(11,0, "HSN / SAC code")
sheet1.write(11,1, hsn_sac)
sheet1.write(12,0, "Place of Supply")
sheet1.write(12,1, place_supply)
sheet1.write(13,0, "TML Part No")
sheet1.write(14,0, "Description of goods or services")
sheet1.write(15,0, "Qty.  & its Unit of Measurement)")
sheet1.write(16,0, "Rate / Unit")
sheet1.write(17,0, "Total Taxable value")
sheet1.write(17,1, total_taxable_f)
sheet1.write(18,0, "Appicable Rate of tax (CGST, SGST(UTGST)/IGST/CESS)")
sheet1.write(18,1, cgst_sgst)
sheet1.write(19,0, "Amount of tax")
sheet1.write(19,1, total_invoice)
sheet1.write(20,0, "Total Invoice value")
sheet1.write(20,1, total_invoice_f)


#wb.save('/home/ujjwal/Downloads/tatadata.xls')
#code for dynamic name with basename
print(name_add)
basename="vedarth_solutions_"
mdate=datetime.datetime.now()
timestr = mdate.strftime("%d-%b-%Y-%H:%M:%S")
filename="/home/ujjwal/pdf_to_text/excel_created/"+basename+timestr+".xls"
wb.save(filename)
