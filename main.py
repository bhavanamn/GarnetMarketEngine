from flask import Flask,render_template,jsonify
import pandas as pd
from datetime import datetime,timedelta
import json

app = Flask(__name__)

symbol_list = ["Nifty 50", "Nifty Bank", "Nifty Financial Services","Reliance"]

@app.route('/')
def index():
    return render_template('index.html',symbol_list=symbol_list)

chart_data = [
    {"time": "2023-10-23","value": 19281.75},
    {"time": "2023-10-24","value": 19290}
]

@app.route('/chart-data')
def get_chart_data():    
    print(f'\x1b[1;36mGetting Dates\x1b[0m\n')
    end_date = datetime.now()
    start_date = end_date - timedelta(500)
    start_timestamp = int(round(datetime.timestamp(start_date),0))
    end_timestamp = int(round(datetime.timestamp(end_date),0))
    print(f'\x1b[1;36mStart Date        \x1b[1;32m{start_date.strftime("%Y-%b-%d")}\x1b[0m')
    print(f'\x1b[1;36mEnd Date          \x1b[1;32m{end_date.strftime("%Y-%b-%d")}\x1b[0m\n')

    nifty_url = f'https://query1.finance.yahoo.com/v7/finance/download/%5ENSEI?period1={start_timestamp}&period2={end_timestamp}&interval=1d&events=history&includeAdjustedClose=true'
    df_nifty50 = pd.read_csv(nifty_url)
    # df_nifty50 = df_nifty50.tail(30).reset_index(drop=True)
    df_nifty50.drop(['Open','High','Low','Adj Close','Volume'],axis=1,inplace=True)
    df_nifty50["Date"] = pd.to_datetime(df_nifty50["Date"])
    chart_data = [{"time": date.strftime("%Y-%m-%d"), "value": close} for date, close in zip(df_nifty50["Date"], df_nifty50["Close"])]
    return jsonify(chart_data)

@app.route('/pred')
def get_pred():
    end_date = datetime.now()
    start_date = end_date - timedelta(500)
    start_timestamp = int(round(datetime.timestamp(start_date),0))
    end_timestamp = int(round(datetime.timestamp(end_date),0))
    print(f'\x1b[1;36mStart Date        \x1b[1;32m{start_date.strftime("%Y-%b-%d")}\x1b[0m')
    print(f'\x1b[1;36mEnd Date          \x1b[1;32m{end_date.strftime("%Y-%b-%d")}\x1b[0m\n')
    nifty_url = f'https://query1.finance.yahoo.com/v7/finance/download/%5ENSEI?period1={start_timestamp}&period2={end_timestamp}&interval=1d&events=history&includeAdjustedClose=true'
    df_nifty50 = pd.read_csv(nifty_url)
    # df_nifty50 = df_nifty50.tail(30).reset_index(drop=True)
    df_nifty50.drop(['Open','High','Low','Adj Close','Volume'],axis=1,inplace=True)
    df_nifty50["Date"] = pd.to_datetime(df_nifty50["Date"])
    df_nifty50 = df_nifty50.tail(1)
    with open('src/prediction.json', 'r') as json_file:
        data = json.load(json_file)
    new_row = {'Date':end_date+timedelta(1),'Close':data['pred_nifty50']}
    df_nifty50.loc[len(df_nifty50)] = new_row
    chart_data = [{"time": date.strftime("%Y-%m-%d"), "value": close} for date, close in zip(df_nifty50["Date"], df_nifty50["Close"])]
    return jsonify(chart_data)


app.run(host='0.0.0.0', port=81)
