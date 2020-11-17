import pymysql
from pymysql.err import IntegrityError

# MOOD_DICT = {"happy": 0, "excited": 1, "ok": 2, "sad": 3, "stressed out": 4}
# MOOD_DICT_REVERSE = {0: "happy", 1: "excited", 2: "ok", 3: "sad", 4: "stressed out"}

# TODO DICTIONARY - IN TELE_BOT.PY
KNOWN_USER_BEGINNING = 0
MOOD_CHECK = 1
KNOWN_USER_MENU = 2
WAITING_FOR_MENU_CHOICE = 3
# AFTER_ONE_CHOICE_BEFORE_NEXT = 4


connection = pymysql.connect(
    host="localhost",
    user="root",
    password="",
    db="sql_intro",
    charset="utf8",
    cursorclass=pymysql.cursors.DictCursor
)


def is_user_in_db(user_id):
    try:
        with connection.cursor() as cursor:
            query = "SELECT COUNT(id) FROM bot_users WHERE id = {}".format(user_id)
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
            if not result['COUNT(id)']:
                return False
            else:
                return True

    except IntegrityError as e:
        message = "error while using is_user_in_db: {}".format(e)
        print(message)


def insert_user(user_id):
    with connection.cursor() as cursor:
        try:
            query = "INSERT INTO bot_users VALUES({}, {}, null)".format(user_id, MOOD_CHECK)
            cursor.execute(query)
            connection.commit()
        except IntegrityError as e:
            message = "error while using insert_user into db: {}".format(e)
            print(message)
            return message


def update_mood(user_id, mood_id):
    with connection.cursor() as cursor:
        try:
            query = "UPDATE bot_users SET mood = {} WHERE id = {}".format(mood_id, user_id)
            cursor.execute(query)
            connection.commit()
        except IntegrityError as e:
            message = "error while using update_mood into db: {}".format(e)
            print(message)
            return message


def get_state(user_id):
    with connection.cursor() as cursor:
        try:
            query = "SELECT state FROM bot_users WHERE id = {}".format(user_id)
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
            return result.get('state')
        except IntegrityError as e:
            message = "error while using get_state into db: {}".format(e)
            print(message)
            return None


def get_mood(user_id):
    with connection.cursor() as cursor:
        try:
            query = "SELECT mood FROM bot_users WHERE id = {}".format(user_id)
            cursor.execute(query)
            result = cursor.fetchone()
            print(result)
            return result.get('mood')
        except IntegrityError as e:
            message = "error while using get_mood into db: {}".format(e)
            print(message)
            return None


# def get_state_as_string():
def set_state(user_id, state_num):
    with connection.cursor() as cursor:
        try:
            query = "UPDATE bot_users SET state = {} WHERE id = {}".format(state_num, user_id)
            cursor.execute(query)
            connection.commit()
        except IntegrityError as e:
            message = "error while using set_state into db: {}".format(e)
            print(message)
            return message


update_mood(1456184694, 1)