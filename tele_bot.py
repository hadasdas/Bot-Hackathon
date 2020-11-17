from client_jokes import get_random_joke


class Bot:
    def __init__(self):
        pass

    def bot_flow(self, text):
        return get_random_joke()
