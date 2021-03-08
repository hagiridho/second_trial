from flask import Flask, jsonify, request, render_template
import json
import pickle
import numpy as np
import pandas as pd

app = Flask(__name__)

model=pickle.load(open("classifier.pkl","rb"))

@app.route('/')
def man():
    return render_template('home.html')
    
@app.route('/predict',methods=["Get"])
def home():
    variance=request.args.get("variance")
    skewness=request.args.get("skewness")
    curtosis=request.args.get("curtosis")
    entropy=request.args.get("entropy")
    arr = np.array([[variance, skewness, curtosis, entropy]])
    pred = model.predict(arr)
    
    print(pred)
    return render_template('after.html', data=pred)

if __name__ == '__main__':
    app.run()