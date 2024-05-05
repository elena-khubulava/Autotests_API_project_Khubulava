import sender_stand_request
import data

def get_new_kit_body(name):
    current_body = data.kit_body.copy()
    current_body["name"] = name
    return current_body

def positive_assert(name):
    new_kit_body = get_new_kit_body(name)
    response = sender_stand_request.post_new_client_kit(new_kit_body)
    assert response.status_code == 201
    assert response.json()["name"] == new_kit_body["name"]


def test_create_kit_2_letter_in_name_get_success_response():
    positive_assert("Aa")
# Test 1
def test_create_kit_1_letter_in_name_get_success_response():
    positive_assert("a")
# Test 2
def test_create_kit_511_letter_in_name_get_success_response():
    positive_assert("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabC")

def negative_assert_symbol(name):
    new_kit_body = get_new_kit_body(name)
    kit_response = sender_stand_request.post_new_client_kit(new_kit_body)

    assert kit_response.status_code == 400
    assert kit_response.json()["code"] == 400
    assert kit_response.json()["message"] == "Тестовое значение для этой проверки будет ниже"
# Test 3
def test_create_kit_no_letters_in_name_get_error_response():
    negative_assert_symbol("")

# Test 4
def test_create_kit_512_letter_in_name_get_error_response():
    negative_assert_symbol("AbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdAbcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcdabcD")

# Test 5
def test_create_kit_english_letter_in_name_get_success_response():
    positive_assert("QWErty")

# Test 6
def test_create_kit_russian_letter_in_name_get_success_response():
    positive_assert("Мария")

# Test 7
def test_create_kit_special_symbol_in_name_get_success_response():
    positive_assert("№%@")

# Test 8
def test_create_kit_space_in_name_get_success_response():
    positive_assert(" Человек и КО ")

# Test 9
def test_create_kit_number_in_name_get_success_response():
    positive_assert("123")

def negative_assert_no_kit_name(name):
    new_kit_body = get_new_kit_body(name)
    response = sender_stand_request.post_new_client_kit(new_kit_body)

    assert response.status_code == 400
    assert response.json()["code"] == 400
    assert response.json()["message"] == "Не все необходимые параметры были переданы"

# Test 10
def test_create_no_kit_name_get_error_response():
    new_kit_body = data.kit_body.copy()
    new_kit_body.pop("name")
    negative_assert_no_kit_name("")

# Test 11
def test_create_user_number_type_in_name_get_error_response():
    new_kit_body = get_new_kit_body(123)
    response = sender_stand_request.post_new_client_kit(new_kit_body)
    assert response.status_code == 400
