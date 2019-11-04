from app import app
from flask import jsonify

@app.route('/')
def index():
    return "<h1>Hello from Flask</h1>"

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