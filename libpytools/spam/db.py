class SessionDB:
    counter = 0
    users = []
    def __init__(self):
        self.roll_back = None

    def save(self, user):
        SessionDB.counter += 1
        user.id = SessionDB.counter
        self.users.append(user)

    def list(self):
        return self.users

    def close(self):
        pass


class Conection:
    def create_session(self):
        return SessionDB()

    def close(self):
        pass