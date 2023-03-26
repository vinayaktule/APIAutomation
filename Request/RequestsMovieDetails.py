import requests

base_url = "https://api.themoviedb.org/3/movie/"
api_key = "0e1d9eac486c2208f38244b104d082d2"


def test_get_top_rated_movies():
    path_param = "top_rated"
    endpoint = base_url + "/" + str(path_param) + "?api_key=" + api_key
    response = requests.get(endpoint)
    assert 200 == response.status_code
