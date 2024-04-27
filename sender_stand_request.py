
import requests

import configuration
import data


def create_order():
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH, json=data.body_create)


body_test = data.body_create.copy()

print(create_order().status_code)


def get_track():
    response = create_order()
    track_number = response.json()["track"]
    return track_number
print(get_track())



def get_order_by_track():
    response = create_order()
    track_number = response.json()["track"]
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "track",
                        json=data.order_data)

print(get_order_by_track())
