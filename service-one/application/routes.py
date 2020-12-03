from application import app
from flask import Flask, render_template, Response
import requests 

@app.route('/', methods=['GET'])   
def index():
    shoe_brand = requests.get("http://localhost:5001/shoe/brand")
    shoe_model = requests.get("http://localhost:5002/shoe/model")
    shoe = shoe_brand.text+" "+str(shoe_model.text)
    return render_template('index.html', title='index', shoe=shoe)	

@app.route('/information/<trainer>', methods=['GET', 'POST'])
def information(trainer):
    information = requests.post('http://localhost:5003/information', data=trainer)
    return render_template('information.html', title='information', trainer=trainer, information=information.text)
