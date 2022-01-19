from django.http import response
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):   
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url=URL,data=json_data)
    data = r.json()
    print(data)

# get_data()

def create_student():
    URL = "http://127.0.0.1:8000/studentapi/"
    data = {
        'name':'naughtyuser',
        'roll':69696,
        'city':'naughtygaziabad',
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    response = r.json()
    print(response)

# create_student()

def update_student():
    URL = "http://127.0.0.1:8000/studentapi/"
    data = {
        'id':2,
        'name':'updateduser',
        'roll':1046,
        'city':'naughty ghaziabad',
    }
    json_data = json.dumps(data)
    r = requests.put(url=URL,data=json_data)
    response = r.json()
    print(response)

# update_student()


def delete_student(id):
    URL = "http://127.0.0.1:8000/studentapi/"
    data = {
        'id':id
    }
    json_data = json.dumps(data)
    r = requests.delete(url=URL,data=json_data)
    response = r.json()
    print(response)

delete_student(1)