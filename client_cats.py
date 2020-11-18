import requests
url = 'http://aws.random.cat/meow'
def get_random_picture():
    payload = "region=us&page=1&language=en&keywords=%5B%22elon%20musk%22%2C%22tesla%22%5D"
    headers = {
        'x-rapidapi-host': "image-video-library.p.rapidapi.com",
        'x-rapidapi-key': "fdd070ac21mshdc7c588ed6d5c28p10b7c0jsnc60eb55bf992",
        'content-type': "application/x-www-form-urlencoded" }

    response = requests.request ("POST", url, data=payload, headers=headers)
    photo_dict = requests.get(url=url).json()
    photo_text = photo_dict.get('love')
    return photo_text

get_random_picture()

"""from IPython.display import Image, display
import requests, json

catURL = 'http://aws.random.cat/meow'

imageURL = json.loads(requests.get(catURL).content)["file"]

img = Image(requests.get(imageURL).content)
display(img)"""

