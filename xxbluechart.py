from flask import Flask, request, render_template

import requests
import json
import math
import datetime

app = Flask(__name__)

@app.route('/')
def root():
    result = requestURL("17088")
    volume = len(result['data']['txOrderbooks']['txOrderbook'])

    '''
    !! 입찰가 판매가 가져올때 필요한 소스 !!

    all_result = result['data']
    page_count = math.ceil(result['recordsTotal'] / 10)

    for i in range(page_count):
        result = requestURL("17088", i)
        all_result.extend(result['data'])
    '''

    '''
    !! 거래량 가져오는 소스 !!

    str(result['data']['txOrderbooks']['txOrderbook'][:10])
    '''

    label = '17088'
    xlabels = []
    dataset = []

    for i in result['data']['txOrderbooks']['txOrderbook'][:volume]:
        xlabels.append(i['tx_date'][:10])
        dataset.append(i['price'])
        
    return render_template('chart.html', **locals())

def requestURL(ProductId):
    params = {
        "rxNo": ProductId,
    }

    res = requests.post("https://xxblue.com/product-detail-ajax", data=json.dumps(params), headers={'Content-Type':'application/json'})
    return json.loads(res.text)

def main():
    app.debug = True
    app.run()

if __name__ == '__main__':
    main()