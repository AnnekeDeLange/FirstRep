from flask import Flask, render_template, redirect, url_for
from flask import request

__winc_id__ = '9263bbfddbeb4a0397de231a1e33240a'
__human_name__ = 'templates'

app = Flask(__name__)

# $env:FLASK_APP="main"
# $env:FLASK_DEBUG=1
# flask run


# @app.route('/<string:name>')
# def title_name(name):
#     breakpoint()
#     return render_template("base.html")


@app.route('/')
def index():
    resp = app.make_response(render_template('index.html',
                                             title="Index"))
    return resp


@app.route('/home')
def home():
    resp = app.make_response(redirect('/', 302))
    resp.url_for('/')
    return resp


@app.route('/about')
def about():
    app.make_response(title='About')
    # render_template("base.html", title_str="Joehoe")
    # return render_template("base.html", title="About", )
    return render_template("about.html", title="About")


# # @app.route('/')
# @app.route('/<string:title_str>')
# def title_string(title_str):
#     print("titelstring is ", title_str)
#     result = render_template('base.html',
#                                  title=title_str)
#     return result
