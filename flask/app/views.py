from app import app
from flask import jsonify
import os

@app.route('/')
def index():

    SECRET_KEY = os.environ.get("SECRET_KEY")
    msg = ''
    if not SECRET_KEY:
        msg = "<h1>Hello from Flask</h1>"
    else:
        msg= f'<h1>Hello from Flask. You secret is {SECRET_KEY}</h1'
    return msg
    
@app.route('/api/products')
def get_products():
    products = [{
        "id": 1,
        "make": "BMW",
        "model": "320",
        "year": 2010,
    },
    {
        "id": 2,
        "make": "Merc",
        "model": "200",
        "year": 2011
    },
    ]
    return jsonify({"products": products})