from flask import Flask, render_template, redirect
# from flask import url_for

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)

# $env:FLASK_APP="main"
# $env:FLASK_DEBUG=1
# flask run


@app.route('/home')
def home():
    response = redirect('/')
    return response


@app.route('/')
def index():
    response = render_template('index.html', title="Index")
    return response


@app.route('/about')
def about():
    response = render_template("about.html",
                               title='About')
    return response


@app.route('/contact')
def contact():
    response = render_template("contact.html",
                               title="Contact")
    return response
