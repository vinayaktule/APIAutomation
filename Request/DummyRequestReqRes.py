import json

import jsonpath
import requests

base_url = "https://reqres.in"


def test_get_req():
    path_param = "/api/users"
    response = requests.get(base_url+path_param)
    print("GET RESPONSE : "+str(response))
    assert response.status_code == 200
    print("-"*50)


def test_post_req():
    path_param = "/api/users"
    file = open('user.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.post(base_url+path_param, request_json)
    print("POST RESPONSE : "+str(response.content))
    assert response.status_code == 201
    response_json = json.loads(response.text)
    assert 'Neo' in jsonpath.jsonpath(response_json, 'name')
    assert 'QA' in jsonpath.jsonpath(response_json, 'job')
    print("-"*50)


def test_put_req():
    path_param = "/api/users/2"
    file = open('user_put.json', 'r')
    json_input = file.read()
    request_json = json.loads(json_input)
    print(request_json)
    response = requests.put(base_url+path_param, request_json)
    print("PUT RESPONSE : "+str(response.content))
    assert response.status_code == 200
    response_json = json.loads(response.text)
    assert 'Neo' in jsonpath.jsonpath(response_json, 'name')
    assert 'QA Automation' in jsonpath.jsonpath(response_json, 'job')
    print("-"*50)


def test_delete_req():
    path_param = "/api/users/2"
    response = requests.delete(base_url+path_param)
    print("DELETE RESPONSE : "+str(response.content))
    assert response.status_code == 204
    print("-"*50)

