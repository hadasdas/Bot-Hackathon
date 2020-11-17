from client_jokes import get_random_joke
import user_db_module as udb
from use_music import get_url_music_by_mood, get_url_music
from bot_speech import speech_dict

HAPPY = 1
SAD = 4


class Bot:

    def __init__(self):
        pass

    def bot_flow(self, text, user_id):
        known_user = udb.is_user_in_db(user_id)
        if not known_user:
            udb.insert_user(user_id)
            udb.set_state(user_id, udb.MOOD_CHECK)
            return speech_dict['welcome'] + speech_dict['mood']

        current_state = udb.get_state(user_id)
        if current_state == udb.KNOWN_USER_BEGINNING:
            udb.set_state(user_id, udb.MOOD_CHECK)
            return speech_dict['see again'] + speech_dict['mood']

        if current_state == udb.MOOD_CHECK:
            udb.set_state(user_id, udb.WAITING_FOR_MENU_CHOICE)
            if text.strip() == "1":
                udb.update_mood(user_id, HAPPY)
                udb.get_mood(user_id)
                return speech_dict["menu_happy"]
            elif text.strip() == "2":
                udb.update_mood(user_id, SAD)
                return speech_dict["menu_sad"]

        if current_state == udb.WAITING_FOR_MENU_CHOICE:
            if text.strip() == "1":
                return speech_dict['bot_will_wait'] + get_random_joke()
            elif text.strip() == "2":
                return speech_dict['bot_will_wait'] + get_url_music_by_mood(user_id)
            else:
                udb.set_state(user_id, udb.KNOWN_USER_BEGINNING)
                return "good_bye"
