import requests

import configuration
import data

def post_new_user(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_USER_PATH,
                         json=body,
                         headers=data.headers)


def get_token():
    response = post_new_user(data.user_body)
    token = response.json()["authToken"]
    return token


def post_new_client_kit(kit_body):
    new_headers = data.headers.copy()
    new_headers["Authorization"] = "Bearer " + get_token()
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_KIT_PATH,
                         json=kit_body,
                         headers=new_headers)



