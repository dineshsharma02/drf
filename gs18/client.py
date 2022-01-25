from django.http import response
import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id=None):   
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.get(url=URL,headers=headers,data=json_data)
    data = r.json()
    print(data)

# get_data(1)

def create_student():
    URL = "http://127.0.0.1:8000/studentapi/"
    data = {
        'name':'Rinesh',
        'roll':199,
        'city':'bhimsar',
    }
    headers = {'content-Type':'application/json'}
    json_data = json.dumps(data)
    r = requests.post(url=URL,headers=headers,data=json_data)
    response = r.json()
    print(response)

# create_student()
# get_data()

def update_student():
    URL = "http://127.0.0.1:8000/studentapi/"
    data = {
        'id':2,
        'name':'updateduser',
        'roll':1046,
        'city':'naughty ghaziabad',
    }
    json_data = json.dumps(data)
    headers = {'content-Type':'application/json'}
    r = requests.put(url=URL,headers=headers,data=json_data)
    response = r.json()
    print(response)

# update_student()
# get_data()


def delete_student(id):
    URL = "http://127.0.0.1:8000/studentapi/"
    data = {
        'id':id
    }
    headers = {'content-Type':'application/json'}

    json_data = json.dumps(data)
    r = requests.delete(url=URL,headers=headers,data=json_data)
    response = r.json()
    print(response)
get_data()
delete_student(1)
get_data()