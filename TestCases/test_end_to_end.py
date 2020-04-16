import json
import os
from pathlib import Path

import requests
from jsonpath import jsonpath

base_url = "http://thetestingworldapi.com/"
dir_name = Path(os.path.dirname(__file__)).parent


def test_end_to_end():
    student_uri = base_url + "api/studentsDetails"
    file = open(os.path.join(dir_name, "student_details.json"), "r")
    testdata_json = json.loads(file.read())

    # create a new student
    response = requests.post(student_uri, testdata_json)
    assert response.status_code == 201
    id = jsonpath(json.loads(response.content), "id")[0]

    skill_uri = base_url + "api/technicalskills/"
    file = open(os.path.join(dir_name, "test_data_skills"), "r")
    skills_data = json.loads(file.read())
    skills_data["id"]= id
    skills_data["st_id"] = id
    print(skills_data)

    response = requests.post(skill_uri, skills_data)
    print(response)
    print(response.content)


test_end_to_end()
