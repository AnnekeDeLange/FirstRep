from flask import Flask
from flask import Response

__winc_id__ = 'cc1b724762854e85a8defa04287f708b'
__human_name__ = 'requests'


app = Flask(__name__)
response = Response()

# aantekeningen
# http://localhost:5000/
# browser openen via Palette: Simple Browser

# $env:FLASK_APP="quickstart"
# $env:FLASK_DEBUG=1
# flask run

# met dir(request) kun je in de (Pdb) opvragen
# wat de keys van een request dictionary zijn.


@app.route('/')
def home():
    return "<p>Home, sweet home.</p>"


@app.route('/greet/')
def greet():
    return "<h1>Hello, world!</h1>"


# variant met variabele url
@app.route('/greet/<string:example_name>')
def greet_name(example_name):
    result = f"<h1>Hello, {example_name}!</h1>"
    return result
