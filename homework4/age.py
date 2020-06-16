import datetime as dt
import requests
from statistics import median
from typing import Optional

from api import get_friends
from api_models import User


def age_predict(user_id: int) -> Optional[float]:
    """ Наивный прогноз возраста по возрасту друзей

    Возраст считается как медиана среди возраста всех друзей пользователя

    :param user_id: идентификатор пользователя
    :return: медианный возраст пользователя
    """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert user_id > 0, "user_id must be positive integer"
    
token = "8b9dad028b9dad028b9dad020c8bec5acf88b9d8b9dad02d5226af134c5f490e61fc588"

def get_friends(user_id, fields):
    """ Returns a list of user IDs or detailed information about a user's friends """
    assert isinstance(user_id, int), "user_id must be positive integer"
    assert isinstance(fields, str), "fields must be string"
    assert user_id > 0, "user_id must be positive integer"
    # PUT YOUR CODE HERE
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

friends = get_friends(187409079, "bdate")

def sorting_func(friend):
  if "bdate" in friend:
    return friend["bdate"].count(".") == 2
  return False

friends_with_bdates = list(filter(sorting_func, friends))


def dates_list(friends):
  dates = [None]*len(friends)
  for (i, fr) in enumerate(friends_with_bdates):
    d, m, y = [int(i) for i in fr["bdate"].split(".")]
    diff = dt.date.today() -  dt.date(y, m, d)
    dates[i] = diff.days//365
  return sorted(dates)

def mean_age(ages):
  return sum(ages)/len(ages)

def median_age(ages):
  l = len(ages)
  if l%2 == 0:
    return (ages[l//2]+ages[l//2+1])/2
  return ages[l//2]

ages = dates_list(friends_with_bdates)

print("средний возраст друга:", mean_age(ages))
print("медианный возраст друга:",median_age(ages))

requests.get(url, params={parameters}, timeout=)


