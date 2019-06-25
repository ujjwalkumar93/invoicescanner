import tempfile, subprocess
# import xlwt
# from xlwt import Workbook


f=open('new_text.txt','w+')

def pdf_to_string(file_object):
    pdfData = file_object.read()
    #f.write(tempfile.NamedTemporaryFile())
    # f.close()
    tf = tempfile.NamedTemporaryFile()
    tf.write(pdfData)
    tf.seek(0)
    outputTf = tempfile.NamedTemporaryFile()

    if (len(pdfData) > 0) :
        out, err = subprocess.Popen(["pdftotext", "-layout", tf.name, outputTf.name ]).communicate()
        #outputTf.read()
        #f.write(outputTf.read())
        #f.close()
        return outputTf.read()
    else :
        return None

pdf_file="Invoice Copy_ Mungi.pdf"
file_object = file(pdf_file, 'rb')
#print(type(pdf_to_string(file_object)))
f.write(pdf_to_string(file_object))
f.close()
print (pdf_to_string(file_object))
print(type(pdf_to_string(file_object)))
