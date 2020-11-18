import requests
import json


def get_random_picture():
    catURL = 'http://aws.random.cat/meow'
    imageURL = json.loads (requests.get (catURL).content)["file"]
    return imageURL


