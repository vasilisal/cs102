import requests
import time

import config


def get(url, params={}, timeout=5, max_retries=5, backoff_factor=0.3):
    """ Выполнить GET-запрос

    :param url: адрес, на который необходимо выполнить запрос
    :param params: параметры запроса
    :param timeout: максимальное время ожидания ответа от сервера
    :param max_retries: максимальное число повторных запросов
    :param backoff_factor: коэффициент экспоненциального нарастания задержки
    """
    delay = 1
    counter = 0
    while counter < max_retries:
        response = requests.get(url, timeout = timeout)
        if response.status_code == CONNECTED:
            break
        sleep(delay)

        delay = min(delay * backoff_factor, timeout)
        delay = delay + normalvariate(delay)
    return response


def get_friends(user_id, fields):
    """ Вернуть данных о друзьях пользователя

    :param user_id: идентификатор пользователя, список друзей которого нужно получить
    :param fields: список полей, которые нужно получить для каждого пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"

    url = "https://api.vk.com/method/friends.get"
    params = {
      "user_id": user_id,
      "fields": fields,
      "access_token": token,
      "test_mode": 1,
      "v":"5.103"
    }
    resp = requests.get(url, params=params)
    return resp.json()["response"]["items"]


def messages_get_history(user_id, offset=0, count=20):
    """ Получить историю переписки с указанным пользователем

    :param user_id: идентификатор пользователя, с которым нужно получить историю переписки
    :param offset: смещение в истории переписки
    :param count: число сообщений, которое нужно получить
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    assert isinstance(offset, int), "offset must be positive integer"
    assert offset >= 0, "user_id must be positive integer"
    assert count >= 0, "user_id must be positive integer"

    url = "https://api.vk.com/method/messages.get"
    params = {
      "user_id": user_id,
      "fields": fields,
      "access_token": token,
      "count": 400,
      "offset": 1 
      "test_mode": 1,
      "v":"5.103"
    }
    resp = requests.get(url, params=params)
    return resp.json()["response"]["items"]

 
