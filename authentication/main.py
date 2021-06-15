import os

from flask import Flask, redirect, render_template
from flask import request, session, url_for, flash
from helpers import get_users, hash_password

__winc_id__ = '8fd255f5fe5e40dcb1995184eaa26116'
__human_name__ = 'authentication'

app = Flask(__name__)

app.secret_key = os.urandom(16)

# to run all this stuf enter the following in the terminal
# $env:FLASK_APP="main"
# $env:FLASK_DEBUG=1
# flask run
# open browser in VSC : CommandPallette>SimpleBrowser
# with url http:/localhost:5000/
# enter or refresh initiates new Request


def valid_login(username, password):
    # username = request.form['username']
    # password = request.form['password']
    user_db = get_users()
    hsd_enterd_pw = hash_password(password)
    # check if user in db
    result = False
    if username in list(user_db.keys()):
        # check if hashed pw matches with db_pw
        if user_db[username] == hsd_enterd_pw:
            result = True
    return result


@app.route('/home')
def redirect_index():
    return redirect(url_for('index'))


@app.route('/')
def index():
    return render_template('index.html', title='Index')


@app.route('/about')
def about():
    return render_template('about.html', title='About')


@app.route('/lon')
def lon():
    return render_template('lon.html', title='League of Nations')


@app.route('/dashboard')
def dashboard():
    if 'username' in session:
        usrname = session['username']
        # print('usrname is', usrname)
        result = render_template('dashboard.html',
                                 title='Dashboard',
                                 name=usrname)
    else:
        flash("Dashboard is only for users that are logged in.")
        result = redirect(url_for('index'))
    return result


@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if valid_login(request.form['username'],
                       request.form['password']):
            session['username'] = request.form['username']
            usrname = session['username']
            flash(f"Welcome {usrname}. You are logged in now.")
            return redirect(url_for('dashboard'))
            # user_db = get_users()
            # current_user = user_db[username]
            # print('current_user is', current_user)
            # return render_template('dashboard.html',
            #                        name=current_user)
        else:
            error = "Invalid username/password"
            redirect(url_for('login', error=True))
    return render_template('login.html', error=error)


# # ORIGINAL EXAMPLE FROM QUICKSTART PAGE
# @app.route('/login', methods=['POST', 'GET'])
# def login():
#     error = None
#     if request.method == 'POST':
#         if valid_login(request.form['username'],
#                        request.form['password']):
#             return log_the_user_in(request.form['username'])
#         else:
#             error = 'Invalid username/password'
#     # the code below is executed if the request method
#     # was GET or the credentials were invalid
#     return render_template('login.html', error=error)
# # END ORIGINAL EXAMPLE FROM QUICKSTART PAGE

# # ORIGINALS in main
# @app.route('/login', methods=['GET', 'POST'])
# def login():
#     # YOUR SOLUTION HERE
#     pass

# @app.route('/dashboard')
# def dashboard():
#     # YOUR SOLUTION HERE
#     pass

# @app.route('/logout', methods=['GET', 'POST'])
# def logout():
#     # YOUR SOLUTION HERE
#     pass
# # END ORIGINALS


@app.route('/logout', methods=['GET', 'POST'])
def logout():
    # usrname = session['username']
    # print(f"Bye, {usrname}, you are logged out now.")
    if "username" in session:
        usrname = session['username']
        # print(f"Bye, {usrname}, you are logged out now.")
        session.pop("username", None)
        flash(f"Bye {usrname}. You were successfully logged out.")
        return redirect(url_for('index'))
    # else:
    return redirect(url_for('index'))
