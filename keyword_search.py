import requests

# リクエストURL設定
req_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Search/20170706?'


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
# 各商品情報から商品名と値段を抽出する。
counter = 0
for i in result['Items']:
    counter += 1
    item = i['Item']
    name = item['itemName']
    print('【No.】' + str(counter))
    print('【Name】' + str(name + '...'))
    print('【Price】' + '¥' + str(item['itemPrice']))
