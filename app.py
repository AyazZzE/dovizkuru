from flask import Flask, render_template
from destek import googlefinance

app = Flask(__name__)

@app.route("/")
def home():
    dolar = googlefinance("USD")
    euro = googlefinance("EUR")
    pound = googlefinance("GBP")
    aud = googlefinance("AUD")
    jpy = googlefinance("JPY")
    frang = googlefinance("CHF")
    türk_lirasi = googlefinance("TRY")
    return render_template("index.html",dolar=dolar, euro=euro, aud=aud, pound=pound, jpy=jpy, frang=frang, türk_lirasi=türk_lirasi)  

   

@app.route("/about")
def about():
    return render_template("about.html")


if __name__ == "__main__":
    app.run(debug=True)


import requests

API_URL = "https://api.exchangeratesapi.io/v1/latest?base="
API_KEY = "dcb5943a9896be799ca051a3c0a1a69f"

response = requests.get(f"{API_URL}USD&apikey={API_KEY}")
data = response.json()
print(data)




