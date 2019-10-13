from flask import Flask, request, render_template, session, redirect
import numpy as np
import pandas as pd


app = Flask(__name__)

f1 = "Resources/cities.csv"
df = pd.read_csv(f1, encoding="ISO-8859-1")

@app.route('/', methods=("POST", "GET"))
def html_table():

    return render_template('simple.html',  tables=[df.to_html(classes='data')], titles=df.columns.values)

if __name__ == '__main__':
    app.run(host='0.0.0.0')