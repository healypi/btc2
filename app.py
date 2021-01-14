from flask import Flask, render_template
import requests
import json
import urllib2
import json 

app = Flask(__name__)

@app.route('/')
def get_bitcoin():
    json_obj = urllib2.urlopen(url)
    data = json.load(json_obj)
    Sats = (data[address]['final_balance'])
    btc = Sats/100000000
    d = btc*34000
    fd = "${:,.2f}".format(d)
    return render_template('index.html', btc=btc)
