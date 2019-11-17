import sqlite3
import http.client
import urllib.parse
import urllib.error
import json


# Initialize the database with three tables: departments, segments, ingredients
def initialize_database():

    conn1 = sqlite3.connect("data/database/ingredients.db")
    cursor = conn1.cursor()
    cursor.execute("""CREATE TABLE IF NOT EXISTS departments
                      (id text primary key, name text,
                      depOrder text)
                   """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS segments
                      (id text primary key, name text, 
                      departmentId text)
                   """)
    cursor.execute("""CREATE TABLE IF NOT EXISTS ingredients
                      (id text primary key, department text, 
                      name text, alternativeSpellings text, createdAt text, updatedAt text)
                   """)

    conn1.commit()
    cursor.close()
    conn1.close()


# get departments
def get_departments():
    headers = {
        'Ocp-Apim-Subscription-Key': 'ba3beeb341524abbac4c500f1a737e1d',
    }
    params = urllib.parse.urlencode({
    })
    try:
        conn = http.client.HTTPSConnection('kesko.azure-api.net')
        conn.request("GET", "/ingredients/departments?%s" % params, "{body}", headers)
        response = conn.getresponse()
        json_obj = json.load(response)
        conn = sqlite3.connect("data/database/ingredients.db")
        cursor = conn.cursor()
        for obj in json_obj:
            array = [obj["id"], obj["name"], obj["order"]]
            cursor.execute("INSERT OR IGNORE INTO departments VALUES (?,?,?)", array)
            conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)


# get segments
def get_segments():
    headers = {
        'Ocp-Apim-Subscription-Key': 'ba3beeb341524abbac4c500f1a737e1d',
    }
    params = urllib.parse.urlencode({
    })
    try:
        conn = http.client.HTTPSConnection('kesko.azure-api.net')
        conn.request("GET", "/ingredients/segments?%s" % params, "{body}", headers)
        response = conn.getresponse()
        json_obj = json.load(response)
        conn = sqlite3.connect("data/database/ingredients.db")
        cursor = conn.cursor()
        for obj in json_obj:
            array = [obj["id"], obj["name"], obj["departmentId"]]
            cursor.execute("INSERT OR IGNORE INTO segments VALUES (?,?,?)", array)
            conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)


# get ingredients
def get_ingredients():
    headers = {
        'Ocp-Apim-Subscription-Key': 'ba3beeb341524abbac4c500f1a737e1d',
    }
    params = urllib.parse.urlencode({
    })
    try:
        conn = http.client.HTTPSConnection('kesko.azure-api.net')
        conn.request("GET", "/ingredients/ingredients?%s" % params, "{body}", headers)
        response = conn.getresponse()
        json_obj = json.load(response)
        conn = sqlite3.connect("data/database/ingredients.db")
        cursor = conn.cursor()
        for obj in json_obj:
            array = [obj["id"], obj["department"], obj["name"],
                     str(obj["alternativeSpellings"]), obj["createdAt"], obj["updatedAt"]]
            cursor.execute("INSERT OR IGNORE INTO ingredients VALUES (?,?,?,?,?,?)", array)
            conn.commit()
        cursor.close()
        conn.close()
    except Exception as e:
        print(e)


initialize_database()
get_departments()
get_segments()
get_ingredients()
