from flask import Flask, render_template, request, send_from_directory
from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    return render_template('home.html')


if __name__ == '__main__':
    app.run(debug=True)
