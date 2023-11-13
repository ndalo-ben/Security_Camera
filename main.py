from flask import Flask,render_template,Response


app=Flask(__name__)
@app.route('/')
def index():
    #rendering webpage
    return render_template('index.html')
def gen():