from application import app
from flask import request, Response
from random import randint

@app.route('/information', methods = ['POST'])
def information():
    trainer = request.data.decode("utf-8")

    if trainer == "Nike Air Force 1":
        price = str(84.95)
    elif trainer == "Nike Dunk":
        price = str(84.95)
    elif trainer == "Nike Air Max 1":
        price = str(99.95)
    elif trainer == "Nike Air Jordan 1":
        price = str(135.00)
    elif trainer == "Adidas SuperStar":
        price = str(80.00)
    elif trainer == "Adidas Ultraboost":
        price = str(139.95)
    elif trainer == "Adidas Gazelle":
        price = str(70.00)
    elif trainer == "Adidas Yeezy":
        price = str(179.95)
    elif trainer == "Asics Gel Lyte-III":
        price = str(95.00)
    elif trainer == "Asics Gel Lyte-V":
        price = str(100.00)
    elif trainer == "Asics Onitsuka Tiger":
        price = str(75.00)
    elif trainer == "Asics Gel-Kayano 5":
        price = str(115.00)
    elif trainer == "New Balance 577":
        price = str(150.00)
    elif trainer == "New Balance 998":
        price = str(200.00)
    elif trainer == "New Balance 827":
        price = str(100.00)
    elif trainer == "New Balance 327":
        price = str(80.00)
    else:
        price = "This trainer does not exist!"
    return Response(price, mimetype= 'text/plain')