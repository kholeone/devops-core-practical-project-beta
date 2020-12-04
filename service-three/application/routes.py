from application import app
from flask import request, Response
from random import randint

@app.route('/shoe/model', methods = ['GET'])
def shoe_model():
    models = ['Air Force 1','Dunk','Air Max 1', 'Air Jordan 1',
		'Superstar', 'Ultraboost', 'Gazelle', 'Yeezy',
			'Gel-Lyte III', 'Gel-Lyte V', 'Onitsuka Tiger', 'Gel-Kayano 5'
				'577', '998', '827', '327']
		
    return Response(models[randint(0,15)], mimetype = 'text/plain')