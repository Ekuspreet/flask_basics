from flask import Flask, render_template, request, redirect, url_for

from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

#Hi
username = "Amrinder singh is a pussy"

@app.route("/", methods = ['POST','GET'])
def welcomeuser():
    return render_template('landing.html')

@app.route("/base", methods = ['GET','POST'])
def base():
    render_template('base.html')

@app.route("/homepage")
def welcomeadmin(username):
    return username

@app.route("/welcome/<name>")
def welcome(name):
    if name != 'admin':
        return redirect(url_for('welcomeuser', username=name))
    else:
        return redirect(url_for('welcomeadmin'))





if __name__ == '__main__':
    app.run(debug=True, port = 8000)
