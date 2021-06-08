from flask import Flask
# from flask import request
from flask import jsonify
# from flask import render_template
app = Flask(__name__)

# aantekeningen
# http://localhost:5000/
# browser openen via Palette: Simple Browser

# $env:FLASK_APP="quickstart"
# $env:FLASK_DEBUG=1
# flask run

# met dir(request) kun je in de (Pdb) opvragen
# wat de keys van een request dictionary zijn.


@app.route('/')
def hello():
    return 'Hou noe jongens!'


# @app.route('/hallo')
# def html_response():
#     return {"message": 'Hallo dames!'}


# variant met variabele url
@app.route('/hallo/<string:name>')
def html_answer(name):
    groet = "Hallo daar, "
    return f"<h1>{groet} {name} !</h1>"


@app.route('/json')
def json_response():
    # return {"message": 'En hier is json stuff!'}
    return jsonify([1, 2, 3])


# @app.rout("/template")
# def template_response():
#     return render_template("plain.html")
