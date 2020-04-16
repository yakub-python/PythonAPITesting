import json
import os
from pathlib import Path

import requests
from jsonpath import jsonpath

dir_name = Path(os.path.dirname(__file__)).parent
base_url = "http://thetestingworldapi.com/"


def test_insert_student():
    uri = base_url + "api/studentsDetails"
    global id
    file = open(os.path.join(dir_name, "student_details.json"), "r")
    testdata_json = json.loads(file.read())

    # create a new student
    response = requests.post(uri, testdata_json)
    assert response.status_code == 201
    id = jsonpath(json.loads(response.content), "id")[0]
    print(str(id))


def test_get_student_details():
    uri = base_url + "api/studentsDetails/" + str(id)
    response = requests.get(uri)
    print(response.status_code)
    print(response.content)
