import json, requests

def ozon_parse(article):
    try:
        price = get_price(article)
    except:
        return False
    data = {
        "price": price[1],
        "photo": price[2],
        "price_card": price[0]
    }
    return data



def get_price(sku):
    cookies = {
        '__Secure-ETC': '8417c8a5d1945b292ae65c249b7938ce',
        '__cf_bm': 'BDuDGAjcDfkH_zgMU3FVTyhMSFWA7FFc6d6ayWjMEYk-1717550553-1.0.1.1-1dIOnca1NhlrqsQqcAyXOL3cZuk9Toptc1MYmtSK.G6Ng7Z5E6JQ8A4ozJTbNZ4JsXAORFc14QwylzLSGU88EA',
        'abt_data': 'a35b70e9c99497cb6051a374c43b2b57:035685afd9505cd8fed26e1e89e13b5098ec73376ded3074245aa21942c09359f43d9f6841d0887fb78542740d91388811ed2a99f736b3615483c47d4aff32ff6968d5ad6a9ebe2aeac2140a12dc76847b83edf2b273ea6de17d8f116e36d36d2e39b36a1076da83c175da5054a0516bd9995915df79c315bd557c35eaf829252febb8a760ed360fe653d77ba20403ab95c336446a0d8f30756fda7d9faf4f4d9050ace2efee52783b350db9e32e681ed48861c040dcc31531fe966b17327e94d742d5f5a964bb5567156d69cf74b43608372154cfc2808678e00735b3421315775c82b90fe6e6e9d9861ff12ddd646f',
        'cf_clearance': '7zx_gpi.GjKhQD04BE4kTTbLo5Vb9txAFHXDi2hIyzs-1717550553-1.0.1.1-bwNdyWDVtzZFN870GkBBkTl59vDyd8LtxXXPWxjpRuSq6TvXnNU8e6ghMTUfFw6mEWZCUTjbSOxdTeTEmXgqfQ',
        '__Secure-ab-group': '58',
        '__Secure-access-token': '4.0.LWRbY4YsTI2IMh006G9MEQ.58.AeG_TXLUtRfJ1YfqifFaAZ6X5MqP2cA4CjB7ZIfD9Mlflow-z7ICHZRmbLZlDQdmjg..20240607234238.byXDv0Vvv8e9e5y5BRXRQyONKQzOFpd0tsY32qu4wzM',
        '__Secure-refresh-token': '4.0.LWRbY4YsTI2IMh006G9MEQ.58.AeG_TXLUtRfJ1YfqifFaAZ6X5MqP2cA4CjB7ZIfD9Mlflow-z7ICHZRmbLZlDQdmjg..20240607234238.qPk8-RxnSm4etavxN8TWt1aUisXlkMkIKP3B2l6i5KA',
        '__Secure-user-id': '0',
        'abt_data': '35e19e449a33afa931cadbd1daa093d6:8f9e4cb0146202e81552086c18be53453315e04654f59b781220672e5808195d112582182c4a06f0ace1755d9abe4cb5adad8b347e995ab79db53d0a35366b27bbf9bb194b6d71a69ef3ad5c75c48dc97946aeebeb004ee15ccd7b729f250ebdbac3502f5e5ee1fe579eeaa45b4c199ff7787de5324fc505639cc84b16c07b0b76fd799fdb52c00f71f1e064fa2f72ef3a4b414623eb5c4feb77da1e67308256363ee69c2ff4c955a76172120b16320b6861b22e6507a0d0e3d1cf153fc09c7529527b3f10cf437593288bbf7d7fa9831472e49bbf345416b3678a46e873d059df8fe5e52e9c15e633b71c2f725ed517ab64b6c025d3989bb3e68cbdd00de54b',
    }

    headers = {
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:126.0) Gecko/20100101 Firefox/126.0',
        'Upgrade-Insecure-Requests': '1',
        'Priority': 'u=1',
        'Accept-Language': 'ru-RU,ru;q=0.8,en-US;q=0.5,en;q=0.3',
        'Sec-Fetch-Site': 'same-origin',
    }

    params = {
        'url': f'/product/{sku}',
        '__rr': '1',
    }

    response = requests.get('https://www.ozon.ru/api/composer-api.bx/page/json/v2', params=params, cookies=cookies, headers=headers)
    js1 = json.loads(response.text)
    js2_s = js1['widgetStates']["webPrice-3121879-default-1"]
    while '\\' in js2_s:
        js2_s.replace("\\", "")
    js2 = json.loads(js2_s)
    try:
        js3_s = str(js1['widgetStates']['webAspects-418255-default-1'])
        a = 0
        if '\\' in js3_s:
            while '''\\''' in js3_s:
                js3_s.replace("\\", "")
                a+=1
                if a == 1000:
                    break
        
        js3 = json.loads(js3_s)
        img=str(js3['aspects'][0]['variants'][0]['data']['coverImage']).replace("wc140", "wc1000")
    except: 
        try:
            js3_s = str(js1['widgetStates']['webGallery-3311629-default-1'])
            js3 = json.loads(js3_s)
            img=str(js3['coverImage'])
        except:
            img=None
        
    price = js2['price'].replace("\u2009", "")
    price = int(price[:-1])
    card_price = js2['cardPrice'].replace("\u2009", "")
    card_price = int(card_price[:-1])

    return [card_price, price, img]
    