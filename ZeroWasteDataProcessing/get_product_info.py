import urllib.parse
import urllib.error
import http.client
import json
import sqlite3
import requests
import pandas as pd
transactions = pd.read_csv('data/tables/df_single_person1_medium.csv', sep=';')
print(transactions.columns)
eans = transactions['EAN'].tolist()

# # The first part, in which we get products
# def get_product(ean1):
#     headers = {'Ocp-Apim-Subscription-Key': 'ba3beeb341524abbac4c500f1a737e1d'}
#     try:
#         r = requests.get('https://kesko.azure-api.net/products/N106/%s' % ean1, data={}, headers=headers)
#         results = r.json()
#         return results
#     except Exception as e:
#         print(e)
#
#
# df_products = pd.DataFrame(columns=['name', 'price', 'ean'])
# products = []
# for ean in eans:
#     item1 = get_product(ean)
#     # info = str(item1)
#     if item1 is not None:
#         name = 'error'
#         price = ''
#         if 'error' not in item1:
#             name = item1['name']
#             price = item1['price']
#     else:
#         name = ''
#         price = ''
#         # info = 'No info'
#     df_product = pd.DataFrame([[name, price, ean]], columns=["name", "price", "ean"])
#     df_products = pd.concat([df_products, df_product])
#     print(len(df_products))
# df_products.to_csv(path_or_buf='data/tables/products.csv', index=False, header=True)


# The second part, in which we filter the products to leave only those that have ingredients
df_products = pd.read_csv(filepath_or_buffer='data/tables/products.csv')
con = sqlite3.connect('data/database/ingredients.db')
df_ingredients = pd.read_sql_query("SELECT name FROM ingredients", con)
ingredients = df_ingredients["name"].tolist()
print(ingredients)
df_chosen = df_products[df_products["name"].isin(ingredients)]
print(df_chosen)
df_chosen.to_csv(path_or_buf='data/tables/products_filtered.csv', index=False, header=True)