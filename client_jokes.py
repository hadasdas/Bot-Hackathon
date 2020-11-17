import requests

JOKE_URL = "https://sv443.net/jokeapi/v2/joke/Any?blacklistFlags=nsfw,racist,sexist"


def get_random_joke():
    querystring = {"format": "json"}

    headers = {
        'x-rapidapi-host': "jokeapi.p.rapidapi.com",
        'x-rapidapi-key': "2444cda1aamsh3bb26a174701e6cp1096d5jsn8b1e663f91e3"
    }

    requests.request("GET", JOKE_URL, headers=headers, params=querystring)
    joke_dict = requests.get(url=JOKE_URL).json()
    joke_text = joke_dict.get('joke')
    if not joke_text:
        joke_text = joke_dict.get('setup')
        joke_text += '\n\n'
        joke_text += joke_dict.get('delivery')

    return joke_text

