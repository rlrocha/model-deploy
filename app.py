# -*- coding: utf-8 -*-
"""
Created on Sat Oct 16 20:21:25 2021

@author: Rafael Rocha
"""

from flask import Flask, render_template, request
import utils as ut

app = Flask(__name__)

@app.route('/', methods = ['GET', 'POST'])
def main():
    
    if request.method == 'POST':
        X_test = request.form['nb']
        X_pred = ut.predictions(X_test)
        
        print(X_pred)
        
    #return 'Hello World'
    return render_template('index.html', my_prediction = X_pred)

# @app.route('/sub', methods=['POST'])
# def submit():
#     # HTML -> .py
#     if request.method == 'POST':
#         name = request.form['username']
        
#     # .py -> HTML
#     return render_template('sub.html', n = name)

if __name__ == '__main__':
    app.run(debug=True)
    #app.run()