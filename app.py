import webbrowser
import sys
import argparse
from os.path import join, realpath
from flask import Flask, render_template, jsonify,request
from flask_sqlalchemy import SQLAlchemy
import warnings
import os
warnings.filterwarnings("ignore")  

sys.path.append(os.path.join(os.getcwd(),'NLU'))
sys.path.append(os.path.join(os.getcwd(),'SpeechToText'))
sys.path.append(os.path.join(os.getcwd(),'TextToSpeech'))
sys.path.append(os.path.join(os.getcwd(),'Wakeword'))

from main import nlu as nl
from speechtotext import speech2text
# from text2speech import say
from wakword import detect_wakeword
app = Flask(__name__)
# app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'

# db=SQLAlchemy(app)




# query=""
@app.route('/',methods=['GET','POST'])
def index():
	if request.method == 'GET':
		return render_template('index.html')
	if request.method == 'POST':
		while True:
#		time.sleep(0.01)
			if detect_wakeword() == True:
				return render_template('wakeword.html')


@app.route('/speech')
def speech():
	# query=speech2text()
	global query 
	# query="hello"
	query=speech2text()
	return render_template('speech.html',query=query)	

@app.route('/nlu')
def nlu():
	result=nl(query)
	# result=query
	return render_template('nlu.html',result=result)

# @app.route('/test')
# def test():
# 	return "test"
# @app.route('/voice/',methods=['GET','POST'])
# def hello():
# 	if request.method == 'GET':
# 		return "bc"
# 	if request.method == 'POST':
# 		while True:
# #		time.sleep(0.01)
# 			if detect_wakeword() == True:
# 				# print("wakeword detected")
# 				query=speech2text()
# 				# print(query)
# 				result=nlu(query)
# 				# print(result)
# 				say(result)


if __name__ == '__main__':
	app.run(debug=True,port=3001)
