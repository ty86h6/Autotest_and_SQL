import configuration
import requests
import data

# Евгения Ямскова, 33-я когорта — Финальный проект. Инженер по тестированию плюс
# Выполнить запрос на создание заказа.
def post_create_new_order(order):
	return requests.post(configuration.URL_SERVICE + configuration.CREATE_ORDER_PATH,
	                     json = order,
	                     headers = data.headers)

# Получение заказа по номеру трекера.
def get_order_from_track(track):
	return requests.get(configuration.URL_SERVICE + configuration.FIND_ORDER_FROM_TRACK_PATH + track,
	                    headers = data.headers)

# Выполнить запрос на получения заказа по треку заказа.
def get_order_from_track_code():
	response_order = post_create_new_order(data.order_body)
	track = response_order.json()["track"]
	return get_order_from_track(track).status_code

# Проверить, что код ответа равен 200.
def test_get_order_from_track_code_200():
	satus_code = get_order_from_track_code()
	assert satus_code == 200