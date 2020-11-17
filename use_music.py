import random
from user_db_module import connection
from pymysql.err import IntegrityError
HAPPY = 1
SAD = 4


def get_url_music(music_type):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT url_music FROM music WHERE id={music_type}"
            cursor.execute(query)
            result = cursor.fetchall()
            random_url_num = random.randint(0, 4)
            return result[random_url_num]['url_music']

    except IntegrityError as e:
        message = "error while using is_user_in_db: {}".format(e)
        print(message)


def get_url_music_by_mood(user_id):
    try:
        with connection.cursor() as cursor:
            query = f"SELECT mood FROM bot_users WHERE id={user_id}"
            cursor.execute(query)
            result = cursor.fetchone()
            mood = result['mood']
            print(result, mood)
            if mood == HAPPY:
                music_type = 2
            else:
                music_type = 1
            return get_url_music(music_type)

    except IntegrityError as e:
        message = "error while using is_user_in_db: {}".format(e)
        print(message)