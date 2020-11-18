import pymysql
from pymysql.err import IntegrityError
from datetime import datetime

DATE0 = datetime(2020, 11, 18)

# MOOD_DICT = {"happy": 0, "excited": 1, "ok": 2, "sad": 3, "stressed out": 4}
# MOOD_DICT_REVERSE = {0: "happy", 1: "excited", 2: "ok", 3: "sad", 4: "stressed out"}


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


def insert_user(user_id, state):
    with connection.cursor() as cursor:
        try:
            query = "INSERT INTO bot_users VALUES({}, {}, null, null)".format(user_id, state)
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


def update_db(user_id, last_choice):
    if last_choice:
        update_last_choice(user_id, last_choice)
        add_user_choice_to_relevant_table(user_id, last_choice)


def update_last_choice(user_id, last_choice):
    with connection.cursor() as cursor:
        try:
            query = "UPDATE bot_users SET last_choice = \'{}\' WHERE id = {}".format(last_choice, user_id)
            cursor.execute(query)
            connection.commit()
        except IntegrityError as e:
            message = "error while using update_last_choice into db: {}".format(e)
            print(message)
            return message


def add_user_choice_to_relevant_table(user_id, last_choice):
    table_name = last_choice + "_users"
    delta = datetime.now() - DATE0
    num_of_days = delta.days
    with connection.cursor() as cursor:
        try:
            query = "INSERT INTO {} VALUES({}, {})".format(table_name, user_id, num_of_days)
            cursor.execute(query)
            connection.commit()
        except IntegrityError as e:
            message = "error while using add_user_choice_to_relevant_table into db: {}".format(e)
            print(message)
            return message


def update_preference(user_id):
    with connection.cursor() as cursor:
        try:
            query = "SELECT last_choice FROM bot_users WHERE id = {}".format(user_id)
            cursor.execute(query)
            result = cursor.fetchone()
            chosen_by_random = result['last_choice']
            add_user_choice_to_relevant_table(user_id, chosen_by_random)

        except IntegrityError as e:
            message = "error while using update_preference into db: {}".format(e)
            print(message)
            return None
