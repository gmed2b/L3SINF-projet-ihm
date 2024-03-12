import requests

def api_query(url, params = None):
  access_token=""
  with open("db.txt", "r") as file:
    access_token = file.read()

  return requests.get(url, headers={"Authorization": f"Bearer {access_token}"}, params=params) 


def api_mutate(url, data, params = None):
  access_token=""
  with open("db.txt", "r") as file:
    access_token = file.read()

  return requests.post(url, headers={"Authorization": f"Bearer {access_token}"}, data=data, params=params)
