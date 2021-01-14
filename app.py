from flask import Flask, render_template
import requests
import json
import urllib3
import json 

app = Flask(__name__)

@app.route('/')
def get_bitcoin():
    address = input('Type or Paste BTC address to reveal balance  ')
    url = 'https://blockchain.info/balance?active='+address+'&?format=hex'
    r = requests.get(url)
    data = r.json()
    Sats = (data[address]['final_balance'])
    btc = Sats/100000000
    d = btc*34000
    fd = "${:,.2f}".format(d)
    return render_template('index.html', btc=btc)


  
