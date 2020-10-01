from flask import Flask,render_template,request
from utility import speak, wishme,openn
import os
app = Flask(__name__)



@app.route('/')
def vai() :
	takecommand()
	return "hello"



if __name__=='__main__':
    app.run(debug=True,port=os.getenv('PORT',5003))