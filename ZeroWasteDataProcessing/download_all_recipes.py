import urllib.parse
import urllib.error
import urllib
import http.client
import json
import requests
import pandas as pd
item_name = 'sausage'
n_recipes = 8065


# get all recipes
def get_recipes(offset, recipes):
    headers = {'Ocp-Apim-Subscription-Key': 'ba3beeb341524abbac4c500f1a737e1d',
               'Content-Type': 'application/json',
    }
    body = {'view': {"offset": offset}}
    print(body)
    params = urllib.parse.urlencode({
    })

    try:

        # conn = http.client.HTTPSConnection('kesko.azure-api.net')
        # conn.request("POST", "/v1/search/recipes?%s" % params, "{body}", headers)
        # response = conn.getresponse()
        # data = response.read()
        # print(data)
        # conn.close()

        r = requests.post('https://kesko.azure-api.net/v1/search/recipes?%s' % params, json=body, headers=headers)
        print(r.json())
        results = r.json()["results"]
        print(len(results))
        for j in range(0, len(results)):
            rec_id = results[j]["Id"]
            Name = results[j]["Name"]
            print(j)
            print(rec_id)
            print(Name)
            PieceSize_Unit = ''
            PieceSize_Amount = ''
            VideoUrl = "None"
            PictureUrl = "None"
            Instructions = ''
            Ingredients = ""
            if 'VideoUrl' in results[j]:
                VideoUrl = results[j]["VideoUrl"]
            if 'PictureUrls' in results[j]:
                if len(results[j]["PictureUrls"]) > 0:
                    PictureUrl = results[j]["PictureUrls"][0]["Normal"]
            if 'Instructions' in results[j]:
                Instructions = results[j]["Instructions"]
            print(Instructions)
            if PieceSize_Unit in results[j]:
                PieceSize_Unit = results[j]['PieceSize']['Unit']
            if 'PieceSize_Amount' in results[j]:
                PieceSize_Amount = results[j]['PieceSize']['Amount']
            if 'IngredientsList' in results[j]:
                IngredientsList = results[j]["Ingredients"]
                if len(IngredientsList) > 0:
                    for i in IngredientsList:
                        for k in i["SubSectionIngredients"]:
                            Ingredients = Ingredients + k[0]["Name"] + '\n'

            print(Ingredients)
            array = pd.DataFrame([[rec_id, Name, PieceSize_Unit, PieceSize_Amount, PictureUrl, VideoUrl, Instructions, Ingredients]],
                                 columns=['Id', 'Name', 'PieceSize_Unit',
                                          'PieceSize_Amount', 'PictureUrl', 'VideoUrl', 'Instructions', 'Ingredients'])
            print(array)
            if array is not None:
                recipes = pd.concat([recipes, array], ignore_index=True)
        return recipes
    except Exception as e:
        print(e)


print(range(0, 8065, 100))
recipes1 = pd.DataFrame(columns=['Id', 'Name', 'PieceSize_Unit', 'PieceSize_Amount', 'PictureUrl', 'VideoUrl', 'Instructions', 'Ingredients'])
# recipes1 = get_recipes(0, recipes1)
for offset1 in range(0, 8065, 100):
    recipes1 = get_recipes(offset1, recipes1)
    print(len(recipes1))
recipes1.to_csv(path_or_buf='data/tables/recipes.csv', index=False, sep=';')
