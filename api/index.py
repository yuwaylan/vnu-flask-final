from flask import Flask
from flask import render_template


app = Flask(__name__)

@app.route('/')
def home():
    return render_template('hi.html')

@app.route('/about')
def about():
    return 'About'
