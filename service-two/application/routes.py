from application import app
from flask import request, Response
from random import randint

@app.route('/shoe/brand', methods = ['GET'])
def shoe_brand():
    shoes = ['Nike','Adidas','Asics','New Balance']
    return Response(shoes[randint(0,3)], mimetype = 'text/plain')

    