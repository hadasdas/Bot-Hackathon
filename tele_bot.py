from client_jokes import get_random_joke
import user_db_module as udb
from use_music import get_url_music_by_mood, get_url_music
from bot_speech import speech_dict
import requests
from config import TOKEN
from time import sleep
from client_cats import get_random_picture
from random import randint


KNOWN_USER_BEGINNING = 0
MOOD_CHECK = 1
WAITING_FOR_MENU_CHOICE = 2
WAITING_FOR_USER_FEEDBACK = 3


def bot_flow(text, user_id):
    known_user = udb.is_user_in_db(user_id)
    if not known_user:
        udb.insert_user(user_id, WAITING_FOR_MENU_CHOICE)
        requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                     .format(TOKEN, user_id, speech_dict['welcome']))
        sleep(3)
        return choose_randomly_between_features_as_hello_greeting(user_id)

    current_state = udb.get_state(user_id)
    func_dict = create_func_dict()
    print(current_state)
    return func_dict[current_state](user_id, text)


def say_hello(user_id, text):
    udb.set_state(user_id, WAITING_FOR_MENU_CHOICE)
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, user_id, speech_dict['see again']))
    sleep(3)
    return choose_randomly_between_features_as_hello_greeting(user_id)


def check_mood(user_id, text):
    feelings_dict = {"happy": 1, "sad": 4, "ok": 3}

    udb.set_state(user_id, WAITING_FOR_MENU_CHOICE)
    if text.strip() == "1":
        udb.update_mood(user_id, feelings_dict["happy"])
        udb.get_mood(user_id)
        return speech_dict["reaction to happy"] + speech_dict["menu"]
    elif text.strip() == "2":
        udb.update_mood(user_id, feelings_dict["sad"])
        return speech_dict["reaction to sad"] + speech_dict["menu"]
    else:
        udb.update_mood(user_id, feelings_dict["ok"])
        return speech_dict["menu sad"]


def choose_options(user_id, text):
    feature_dict = {1: "joke", 2: "music", 3: "cat_pic"}
    cat_pic = False
    random_feature = False
    string_num = text.strip()
    if string_num == "1":
        first_answer = get_random_joke()
    elif string_num == "2":
        first_answer = get_url_music_by_mood(user_id)
    elif string_num == "3":
        first_answer = get_random_picture()
        cat_pic = True
    elif string_num == "4":
        first_answer = choose_randomly_between_features(user_id, feature_dict)
        udb.set_state(user_id, WAITING_FOR_USER_FEEDBACK)
        random_feature = True
    else:
        udb.set_state(user_id, KNOWN_USER_BEGINNING)
        return speech_dict["good bye"]

    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, user_id, first_answer))
    # updating db: last choice of feature, tables tah belong to each feature:
    # if choosing random shuffle - this function sends None as second feature
    udb.update_db(user_id, feature_dict.get(int(string_num)))
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
    func_dict = {1: get_random_joke, 2: get_url_music, 3: get_random_picture}
    index = randint(1, len(func_dict))
    udb.update_last_choice(user_id, feature_dict[index])
    return func_dict[index]()


def choose_randomly_between_features_as_hello_greeting(user_id):
    udb.set_state(user_id, MOOD_CHECK)
    func_list = [get_random_joke, get_random_picture]
    index = randint(0, len(func_list)-1)
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, user_id, func_list[index]()))
    sleep(5)
    return speech_dict['mood']


def create_func_dict():
    func_dict = {KNOWN_USER_BEGINNING: say_hello,
                 MOOD_CHECK: check_mood,
                 WAITING_FOR_MENU_CHOICE: choose_options,
                 WAITING_FOR_USER_FEEDBACK: get_feedback}

    return func_dict


def get_feedback(user_id, text):
    udb.set_state(user_id, WAITING_FOR_MENU_CHOICE)
    if text.strip() == "1":
        udb.update_preference(user_id)

    return speech_dict['bot is waiting']
