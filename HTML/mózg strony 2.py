from flask import Flask, redirect, url_for, render_template
import csv
import pandas as pd

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("base.html")

@app.route("/dane")
def dane_pandas():
	df = pd.read_csv('/Users/joachimuetake/SW projekt/dane_bez_spacji.csv', sep='/')
	return render_template('tabela_pandas.html', df=df)

if __name__ == "__main__":
    app.run(debug=True)