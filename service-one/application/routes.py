from application import app
from flask import Flask, render_template, Response
import requests 

@app.route('/', methods=['GET'])   
def index():
    shoe_brand = requests.get("http://service-two:5001/shoe/brand")
    shoe_model = requests.get("http://service-three:5002/shoe/model")
    shoe = shoe_brand.text+" "+str(shoe_model.text)
    return render_template('index.html', title='index', shoe=shoe)	

@app.route('/information/<trainer>', methods=['GET', 'POST'])
def information(trainer):
    information = requests.post('http://service-four:5003/information', data=trainer)
    return render_template('information.html', title='information', trainer=trainer, information=information.text)
