from client_jokes import get_random_joke
import user_db_module as udb
from use_music import get_url_music_by_mood, get_url_music
from bot_speech import speech_dict
import requests
from config import TOKEN
from time import sleep


def bot_flow(text, user_id):
    known_user = udb.is_user_in_db(user_id)
    if not known_user:
        udb.insert_user(user_id)
        return speech_dict['welcome'] + speech_dict['mood']

    current_state = udb.get_state(user_id)
    func_dict = create_func_dict()
    return func_dict[current_state](user_id, text)


def say_hello(user_id, text):
    udb.set_state(user_id, udb.MOOD_CHECK)
    return speech_dict['see again'] + speech_dict['mood']


def check_mood(user_id, text):
    feelings_dict = {"happy": 1, "sad": 4, "ok": 3}

    udb.set_state(user_id, udb.WAITING_FOR_MENU_CHOICE)
    if text.strip() == "1":
        udb.update_mood(user_id, feelings_dict["happy"])
        udb.get_mood(user_id)
        return speech_dict["menu happy"]
    elif text.strip() == "2":
        udb.update_mood(user_id, feelings_dict["sad"])
        return speech_dict["menu sad"]
    else:
        udb.update_mood(user_id, feelings_dict["ok"])
        return speech_dict["menu sad"]


def choose_options(user_id, text):
    if text.strip() == "1":
        first_answer = get_random_joke()
    elif text.strip() == "2":
        first_answer = get_url_music_by_mood(user_id)
    else:
        udb.set_state(user_id, udb.KNOWN_USER_BEGINNING)
        return speech_dict["good bye"]
    requests.get("https://api.telegram.org/bot{}/sendMessage?chat_id={}&text={}"
                 .format(TOKEN, user_id, first_answer))
    sleep(4)
    return speech_dict['bot is waiting']


def create_func_dict():
    func_dict = {udb.KNOWN_USER_BEGINNING: say_hello,
                 udb.MOOD_CHECK: check_mood,
                 udb.WAITING_FOR_MENU_CHOICE: choose_options}

    return func_dict
