import requests

# リクエスト情報設定
req_url = 'https://app.rakuten.co.jp/services/api/Product/Search/20170426?'

# リクエスト情報設定
keyword = input('検索キーワードを入力してください。')
serch_params = {
    "format": "json",
    "keyword": keyword,
    "applicationId": '1006832436076307428',
    "hits": 10,
    "page": 1,
}

# リクエスト実行
response = requests.get(req_url, serch_params)

# レスポンスファイルをjson化
result = response.json()

# 検索内容出力処理
# 各商品情報から商品名と最安値、最高値を抽出する。
counter = 0
for i in result['Products']:
    counter += 1
    Product = i['Product']
    name = Product['productName']
    maxPrice = Product['maxPrice']
    minPrice = Product['minPrice']

    print('【No.】' + str(counter))
    print('【Name】' + str(name + '...'))
    print('【最安値】' + '¥' + str(minPrice))
    print('【最高値】' + '¥' + str(maxPrice))
