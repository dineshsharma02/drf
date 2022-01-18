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
    URL = "http://127.0.0.1:8000/createstudent/"
    data = {
        'name':'newuser',
        'roll':1111,
        'city':'naughtygaziabad',
    }
    json_data = json.dumps(data)
    r = requests.post(url=URL,data=json_data)
    response = r.json()
    print(response)

create_student()