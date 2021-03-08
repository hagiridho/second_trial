# -*- coding: utf-8 -*-
"""
Created on Mon Mar  8 17:26:34 2021

@author: Hagi
"""

from flask import Flask, render_template

app = Flask(__name__)

@app.route('/home')
def home():
    return "<h1>hello</h1>"

if __name__ == '__main__':
    app.run()