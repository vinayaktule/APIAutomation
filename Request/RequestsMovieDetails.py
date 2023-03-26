import json

import pytest
import requests
from requests.auth import HTTPBasicAuth

base_url = "https://api.themoviedb.org/3/movie"
api_key_v4 = "0e1d9eac486c2208f38244b104d082d2"
api_key_v3 = "eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiIwZTFkOWVhYzQ4NmMyMjA4ZjM4MjQ0YjEwNGQwODJkMiIsInN1YiI6IjY0MWM1Y2I2ZDc1YmQ2MjRhNTgxNDUzMiIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.PaxXsDfuSdkknh3x2zuRXQLZ8JnvddcG97Li0nN7TaY"


# TODO : get response
def test_get_top_rated_movies():
    path_param = "top_rated"
    endpoint = base_url + "/" + str(path_param) + "?api_key=" + api_key_v4
    # https://api.themoviedb.org/3/movie/top_rated/?api_key=0e1d9eac486c2208f38244b104d082d2
    response = requests.get(endpoint)
    assert response.status_code == 200
    print("-" * 50)


# TODO : post request
def test_rate_movie():
    path_param = 550
    endpoint = f"https://api.themoviedb.org/3/movie/{path_param}/rating/"
    print(endpoint)
    headers = {'Accept': 'application/json'}
    payload = {'value': 8.5}
    auth = HTTPBasicAuth('apikey', api_key_v4)
    response = requests.post(endpoint, auth=auth, data=payload)
    print(response.json())
    # assert response.status_code == 201
    assert response.json()[0].status_message == 'Success.'
    print("-" * 50)

