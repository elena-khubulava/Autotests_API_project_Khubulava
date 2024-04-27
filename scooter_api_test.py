import requests

import configuration
import sender_stand_request

import data


# Elena Khubulava final project autotest 15-Venus
def test_succsess_order_create():
    response = sender_stand_request.create_order()
    track_number = response.json()["track"]
    assert response.status_code == 201


def test_get_order_by_track():
    response = sender_stand_request.create_order()
    track_number = response.json()["track"]
    return track_number
    return requests.get(configuration.URL_SERVICE + configuration.GET_ORDER_PATH + "t",
                        json=data.order_data)

    assert response.status_code == 200
