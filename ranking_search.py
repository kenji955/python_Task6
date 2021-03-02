import requests
import pandas as pd
import numpy as np


# リクエスト情報設定
req_url = 'https://app.rakuten.co.jp/services/api/IchibaItem/Ranking/20170628?'

# リクエスト情報設定
serch_params = {
    "format": "json",
    "applicationId": '1006832436076307428',
    "page": 1,
}

# リクエスト実行
response = requests.get(req_url, serch_params)

# レスポンスファイルをjson化
result = response.json()
# print(result)

item_key = ['rank', 'itemName', 'itemPrice', 'itemUrl',
            'reviewCount', 'reviewAverage', 'shopName', 'shopUrl']
item_list = []
for i in range(0, len(result['Items'])):
    tmp_item = {}
    item = result['Items'][i]['Item']
    for key, value in item.items():
        if key in item_key:
            tmp_item[key] = value
    item_list.append(tmp_item)
# データフレームを作成
items_df = pd.DataFrame(item_list)

# 列の順番を入れ替える
items_df = items_df.reindex(
    columns=['rank', 'itemName', 'itemPrice', 'itemUrl',
             'reviewCount', 'reviewAverage', 'shopName', 'shopUrl'])

# 列名と行番号を変更する:列名は日本語に、行番号は1からの連番にする
items_df.columns = ['順位', '商品名', '商品価格', '商品URL',
                    'レビュー数', 'レビュー平均', '店舗名', '店舗URL']
items_df.index = np.arange(1, 31)

items_df.to_csv('result.csv')
# 検索内容出力処理
# 各商品情報から商品名と最安値、最高値を抽出する。
# counter = 0
# for i in result['Products']:
#     counter += 1
#     Product = i['Product']
#     name = Product['productName']
#     maxPrice = Product['maxPrice']
#     minPrice = Product['minPrice']

#     print('【No.】' + str(counter))
#     print('【Name】' + str(name + '...'))
#     print('【最安値】' + '¥' + str(minPrice))
#     print('【最高値】' + '¥' + str(maxPrice))
