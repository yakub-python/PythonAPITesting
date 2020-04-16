import json
import os
from pathlib import Path

import requests

base_url = "http://thetestingworldapi.com/"
dir_name = Path(os.path.dirname(__file__)).parent


# GET Method
def test_get_all_student_details():
    resource_uri = "api/technicalskills"
    response = requests.get(base_url + resource_uri)

    print(response.status_code)
    print("-----------------------------------------")
    print(response.content)
    print("-----------------------------------------")
    print(json.loads(response.text))
    assert response.status_code == 200


# GET Method
def test_get_student_details_using_id():
    resource_uri = base_url + "api/technicalskills/10947"
    response = requests.get(resource_uri)

    print(response.status_code)
    print("-----------------------------------------")
    print(response.content)
    print("-----------------------------------------")
    print(json.loads(response.text))
    assert response.status_code == 200


def test_write_json_respose_to_a_file():
    resource_uri = base_url + "api/technicalskills/10947"
    response = requests.get(resource_uri)
    respose_json = json.loads(response.text)

    file = open(os.path.join(dir_name, "test_data_skills"), "w")
    file.write(json.dumps(respose_json))


# PUT Method
def test_update_skills():
    resource_uri = base_url + "api/technicalskills/10947"
    file = open(os.path.join(dir_name, "test_data_skills"), "r")
    test_data_json = json.loads(file.read())

    response = requests.get(resource_uri, test_data_json)
    print(response.status_code)
    print(response.content)
    assert response.status_code == 200


# POST Method
def test_add_new_skill():
    resource_uri = base_url + "api/technicalskills/"
    file = open(os.path.join(dir_name, "test_data_skills"), "r")
    test_data_json = json.loads(file.read())
    print(test_data_json)
    response = requests.post(resource_uri, test_data_json)
    print(response.status_code)
    print(response.content)
    print(response.text)
    print(response.headers)
    # assert response.status_code == 200
