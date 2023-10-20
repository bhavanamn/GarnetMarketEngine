from flask import Flask,render_template

app = Flask(__name__)

symbol_list = ["Nifty 50", "Nifty Bank", "Nifty Financial Services","Reliance"]

@app.route('/')
def index():
    return render_template('index.html',symbol_list=symbol_list)


app.run(host='0.0.0.0', port=81)
