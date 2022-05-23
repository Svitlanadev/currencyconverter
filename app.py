from flask import Flask
from flask import render_template
import requests as req
import json

app = Flask(__name__)


@app.route('/convert/')
@app.route('/convert/<base>/<to>/<amount>')


def convert(base=None, to=None, amount=None):
    currency = base + to
    response = req.get('https://api.finage.co.uk/last/forex/'+currency+'?apikey=API_KEY2bdqbZFgkKEQHAVbg5qmGhZnJ40ygskmr3v1Uft70UJEZk')
    body = json.loads(response.text)
    koef = body["bid"]
    result = int(amount) * koef
    return render_template("index.html", base=base, to=to, amount=amount, result=result)

if __name__ == '__main__':
    app.run(debug=True)


