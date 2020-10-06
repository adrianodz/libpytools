from time import sleep


class SessionDB:
    counter = 0
    users = []

    def save(self, user):
        SessionDB.counter += 1
        user.id = SessionDB.counter
        self.users.append(user)

    def list(self):
        return self.users

    def roll_back(self):
        self.users.clear()

    def close(self):
        pass


class Conection:

    def __init__(self):
        sleep(1)

    def create_session(self):
        return SessionDB()

    def close(self):
        pass
