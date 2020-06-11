from flask import Flask, request, render_template

import requests
import json
import math

app = Flask(__name__)

@app.route('/')
def root():
    produtcId = '17088'
    request_Data = requestUrl(produtcId)
    volume = len(request_Data['data']['txOrderbooks']['txOrderbook'])

    label = produtcId
    send_Data = request_Data['data']['txOrderbooks']['txOrderbook'][:volume]
    
    '''
    !! 입찰가 판매가 가져올때 필요한 소스 !!

    all_result = result['data']
    page_count = math.ceil(result['recordsTotal'] / 10)

    for i in range(page_count):
        result = requestUrl("17088", i)
        all_result.extend(result['data'])
    
    !! 파이썬에서 자료 처리하여 html로 넘기는 소스 !!
    xlabels = []
    dataset = []
    size = []
    useful_size = []
    
    for result_Data in request_Data['data']['txOrderbooks']['txOrderbook'][:volume]:
        size.append(result_Data['product_option'])
        if result_Data['product_option'] == '260':
            xlabels.append(result_Data['tx_date'][:10])
            dataset.append(result_Data['price'])
        
    xlabels.reverse()
    dataset.reverse()
    size.reverse()
    useful_size = sorted(list(set(size)))
    '''

    return render_template('chart.html', **locals())

def requestUrl(ProductId):
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