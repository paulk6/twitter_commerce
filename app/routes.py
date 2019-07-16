from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():
    products = [
        {
            'id': 1001,
            'title': 'Soap',
            'price': '3.98',
            'desc': 'Very clean soapy soap. Has soapness.'
        },
        {
            'id': 1002,
            'title': 'Grapes',
            'price': '2.50',
            'desc': 'Very clean soapy grapes. Has grapeness. Cleans your insides!'
        },
        {
            'id': 1003,
            'title': 'A Video Game',
            'price': '60',
            'desc': 'Very clean video gamey video game. Has game.'
        },
        {
            'id': 1004,
            'title': 'Happiness',
            'price': '100',
            'desc': 'Very clean happy times. Has good feels.'
        },
    ]

    return render_template('index.html', products=products, title='Home')


@app.route('/checkout')
def checkout():
    return render_template('checkout.html', title='Checkout')


@app.route('/title')
def title():
    return render_template('form.html', title='Change Title')
