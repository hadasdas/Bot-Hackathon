from client_jokes import get_random_joke
import user_db_module as udb
from music_db_module import get_url_music_by_mood, get_url_music
from bot_speech import speech_dict
import requests
from config import TOKEN  # , NGROK_URL
from time import sleep
from client_cats import get_random_picture
from random import randint
# import json


KNOWN_USER_BEGINNING = 0
AFTER_MOOD_CHECK = 1
CHOOSING_FROM_MENU = 2
WAITING_FOR_USER_FEEDBACK = 3

# MOODS:
HAPPY = 1
OK = 3
SAD = 4

# FEATURES:
JOKE = 1
MUSIC = 2
CAT_PIC = 3
LAUGHTER = 4
SHUFFLE = 5

UPBEAT_MUSIC_CHOICE = 7
MUSIC_LIKE_MOOD_MELLOW = 8


def bot_flow(text, user_id):
    known_user = udb.is_user_in_db(user_id)
    if not known_user:
        udb.insert_user(user_id)
        requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                     .format(TOKEN, user_id, speech_dict['welcome']))
        sleep(3)
        return choose_randomly_between_features_as_hello_greeting(user_id)

    current_state = udb.get_state(user_id)
    func_dict = create_func_dict()
    print(current_state)
    return func_dict[current_state](user_id, text)


def create_func_dict():
    func_dict = {KNOWN_USER_BEGINNING: say_hello,
                 AFTER_MOOD_CHECK: check_mood,
                 CHOOSING_FROM_MENU: choose_options,
                 WAITING_FOR_USER_FEEDBACK: get_feedback}

    return func_dict


def say_hello(user_id, text):
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, user_id, speech_dict['see again']))
    sleep(3)
    return choose_randomly_between_features_as_hello_greeting(user_id)


def check_mood(user_id, text):
    udb.set_state(user_id, CHOOSING_FROM_MENU)
    if text.strip() == "1":
        udb.update_mood(user_id, HAPPY)
        return speech_dict["reaction to happy"] + speech_dict["menu"]
    elif text.strip() == "2":
        udb.update_mood(user_id, SAD)
        return speech_dict["reaction to sad"] + speech_dict["menu"]
    else:
        udb.update_mood(user_id, OK)
        return speech_dict["reaction to sad"] + speech_dict["menu"]


def choose_options(user_id, text):
    feature_dict = {1: "joke", 2: "music", 3: "cat_pic", 4: "laughter"}
    cat_pic = False
    random_feature = False
    string_num = text.strip()
    if string_num == str(JOKE):
        first_answer = get_random_joke()
    elif string_num == str(MUSIC) or string_num == str(MUSIC_LIKE_MOOD_MELLOW):
        if udb.get_mood(user_id) >= OK and string_num != str(MUSIC_LIKE_MOOD_MELLOW): # >= OK means - not such a great mood
            return speech_dict['choose music']
        first_answer = get_url_music_by_mood(user_id)
    elif string_num == str(CAT_PIC):
        first_answer = get_random_picture()
        cat_pic = True
    elif string_num == str(LAUGHTER):
        first_answer = get_laughter()
    elif string_num == str(SHUFFLE):
        first_answer = choose_randomly_between_features(user_id, feature_dict)
        udb.set_state(user_id, WAITING_FOR_USER_FEEDBACK)
        random_feature = True
    elif string_num == str(UPBEAT_MUSIC_CHOICE):
        first_answer = get_url_music_by_mood(user_id, True)

    else:
        udb.set_state(user_id, KNOWN_USER_BEGINNING)
        return speech_dict["good bye"]

    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, user_id, first_answer))
    feature_index = int(string_num)
    if string_num == str(UPBEAT_MUSIC_CHOICE) or string_num == str(MUSIC_LIKE_MOOD_MELLOW):
        feature_index = 2  # music index. these are callbacks from the music option
    # updating db: last choice of feature, tables tah belong to each feature:
    # if choosing random shuffle - this function sends None as second feature
    udb.update_db(user_id, feature_dict.get(feature_index))
    if cat_pic:
        sleep(5)
        # adding an "awhhh" message after cat picture:
        requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                     .format(TOKEN, user_id, speech_dict['cat awh']))
    if random_feature:
        sleep(5)
        return speech_dict['get feedback']
    sleep(5)
    return speech_dict['bot is waiting']


def choose_randomly_between_features(user_id, feature_dict):
    func_dict = {1: get_random_joke, 2: get_url_music, 3: get_random_picture, 4: get_laughter}
    index = udb.get_random_index_according_to_db_preferences(user_id)
    udb.update_last_choice_after_shuffle(user_id, feature_dict[index])
    return func_dict[index]()


def choose_randomly_between_features_as_hello_greeting(user_id):
    udb.set_state(user_id, AFTER_MOOD_CHECK)
    func_list = [get_random_joke, get_random_picture, get_laughter]
    index = randint(0, len(func_list)-1)
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, user_id, func_list[index]()))
    sleep(5)
    return speech_dict['mood']


def get_feedback(user_id, text):
    udb.set_state(user_id, CHOOSING_FROM_MENU)
    if text.strip() == "1":
        udb.update_preference(user_id)

    return speech_dict['bot is waiting']


def get_laughter():
    return "https://www.youtube.com/watch?v=3TWpPrcl0WY"

"""
def get_image():
    image = json.loads(requests.get("{}/image2.jpg".format(NGROK_URL)).content)["file"]
    return image
"""