import os
#from qrtools import QR 
# import StringIO
# from reportlab.pdfgen import canvas
# from reportlab.lib.pagesizes import letter
#import file
from flask_sqlalchemy import SQLAlchemy
from flask import request,Flask, render_template, url_for, flash, redirect, send_from_directory
#from forms import RegistrationForm, LoginForm, MyLoginForm
#from plot import do_plot
from flask import Flask, send_file, make_response 
import urllib.request
import json
from flask_bootstrap import Bootstrap
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

app = Flask(__name__)


app.config['SECRET_KEY']= 'c698baeb61c95d216dc24d8254331da1'
app.config['SQLALCHEMY_DATABASE_URI']='/sqlite:///site.db'

db=SQLAlchemy(app)


@app.route("/",methods=['GET','POST'])
@app.route("/home",methods=['GET','POST'])
def home_test():
    if request.method=='POST':
        filename=request.form['myfile']
        string=""
        string+=filename
        print(filename)
        rsrcmgr = PDFResourceManager()
        sio = BytesIO()
        codec = 'utf-8'
        laparams = LAParams()
        device = TextConverter(rsrcmgr, sio, codec=codec, laparams=laparams)
        interpreter = PDFPageInterpreter(rsrcmgr, device)
        fp = open(string, 'rb')
        for page in PDFPage.get_pages(fp):
            interpreter.process_page(page)
        fp.close()
        text = sio.getvalue()
        #text=text.replace(chr(272)," ")
        print(type(text))
        f = open('final2.txt','wb')
        f.write(text)
        print("hello")
        fobj = open("final2.txt")
        text = fobj.read().strip().split()
        print(text)
        if 'Customer' in open('final2.txt','r').read():
            print("true")
        # while True:
        #     s="Customer PO"
        #     if s=="":
        #         print("No string entered")
        #         break
        #     if s in text:
        #         print("Matched")
        #         break
        #     else:
        #         print("No such string found")
        #         break
        # fobj.close()
        print("SEE ABOVE")   
        os.system("python2 new.py")
        os.system("python2 add_t_pdf.py")      
    return render_template('home.html')

@app.route("/list")
def list():
    return render_template('list.html')


 
if __name__== '__main__':
 	app.run(debug=True)   


