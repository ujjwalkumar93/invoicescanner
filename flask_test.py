import os
import re
import glob
#import pdftotext
import PyPDF2
import shutil
#import textract
#from nltk.tokenize import word_tokenize
#from nltk.corpus import stopwords
#from qrtools import QR
# import StringIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
#import file
#from flask_sqlalchemy import SQLAlchemy
from flask import request,Flask, render_template, url_for, flash, redirect, send_from_directory
#from forms import RegistrationForm, LoginForm, MyLoginForm
#from plot import do_plot
from flask import Flask, send_file, make_response
import urllib.request
import json
#from flask_bootstrap import Bootstrap
import pickle
import re
import numpy as np
from numpy import array

from io import BytesIO
from io import StringIO

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams
from pdfminer.pdfpage import PDFPage

app = Flask(__name__,static_folder='excel_created')


app.config['SECRET_KEY']= 'c698baeb61c95d216dc24d8254331da1'
# app.config['SQLALCHEMY_DATABASE_URI']='/sqlite:///site.db'

# db=SQLAlchemy(app)


@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def home_test():
    if request.method=='POST':
        f=request.files['myfile']
        fname=f.filename
        f.save(f.filename)
        #string=""
        #string+=filename
        #print(filename)
        #print("SEE FILE NAME ABOVE")
        # print("SEE ABOVE")
        # line_number = 27#I understood you know this. right ?
        # string_to_add =filename#I understood you know this. right ?
        # string_to_find = "pdf_file="#I understood you know this. right ?
        # filename = "test2.py"
        # with open(filename,"r") as f:
        #     s = f.readlines()
        # s[line_number] = s[line_number].replace(string_to_find,string_to_find+string_to_add)
        # with open(filename,"w") as f:
        #     for line in s:
        #         f.write(line)
        # with open('test2.py', 'r') as f:
        #     print(f.read())
        # with open('test2.py', 'w') as f:
        #     lines = f.readlines()
        #     for i, line in enumerate(lines):
        #         if line.startswith('pdf_text='):
        #             line[i] = line[i].strip() + filename+'\n'
        #     f.seek(0)
        #     for line in lines:
        #         f.write(line)
        text='pdf_file="'+fname+'"'
        print(text)
        print(type(text))
        print("*****************")
        temp = open('temp', 'w+')
        with open('test2.py', 'r') as f:
            for line in f:
                if line.startswith('pdf_file='):
                    line = '\n'
                    line=line.strip()+text+'\n'
                temp.write(line)
        temp.close()
        shutil.move('temp', 'test2.py')

        os.system("python2 test2.py")
        os.system("sudo python3 pdftoexcel_n.py")
    return render_template('home.html')

# @app.route('/', defaults={'req_path': ''})
# @app.route('/<path:req_path>')
@app.route("/list",methods = ['POST', 'GET'])
def dir_listing():
    dir=os.getcwd()
    files=os.listdir(dir+"/excel_created")
    return render_template('list.html',files=files)

# @app.route('/file-downloads/')
# def file_downloads():
#     try:
#         return render_template('downloads.html')
#     except Exception as e:
#         return str(e)

# @app.route('/return-files/')
# def return_files_tut():
#     try:
#         return send_file('/home/tushar/pdf_to_text/downloads/Invoice1-converted.xlsx', attachment_filename='Invoice1-converted.xlsx')
#     except Exception as e:
#         return str(e)

@app.route('/pdf/<path:filename>', methods=['GET', 'POST'])
def download(fname):
    return send_from_directory(directory='pdf', filename=fname)


if __name__== '__main__':
 	app.run(debug=True)




# import tempfile, subprocess
# # import xlwt
# # from xlwt import Workbook


# f=open('new_text.txt','w')

# def pdf_to_string(file_object):
#     pdfData = file_object.read()
#     #f.write(tempfile.NamedTemporaryFile())
#     # f.close()
#     tf = tempfile.NamedTemporaryFile()
#     tf.write(pdfData)
#     tf.seek(0)
#     outputTf = tempfile.NamedTemporaryFile()

#     if (len(pdfData) > 0) :
#         out, err = subprocess.Popen(["pdftotext", "-layout", tf.name, outputTf.name ]).communicate()
#         #outputTf.read()
#         #f.write(outputTf.read())
#         #f.close()
#         return outputTf.read()
#     else :
#         return None

# pdf_file="Invoice1.pdf"
# file_object = file(pdf_file, 'rb')
# #print(type(pdf_to_string(file_object)))
# f.write(pdf_to_string(file_object))
# f.close()
# print (pdf_to_string(file_object))
# print(type(pdf_to_string(file_object)))
