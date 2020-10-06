from libpytools.spam.db import Conection
from libpytools.spam.models import User


def test_save_user():
    conection = Conection()  # responsible for authenticate the user of DB
    session = conection.create_session()  # session is used to manipulate the DB
    user = User(name='Adriano')
    session.save(user)
    assert isinstance(user.id, int)
    session.roll_back()  # destroy all modifications
    session.close()
    conection.close()

def test_list_user():
    conection = Conection()  # responsible for authenticate the user of DB
    session = conection.create_session()  # session is used to manipulate the DB
    users = [User(name='Adriano'), User(name='Luciano')]
    for user in users:
        session.save(user)
    assert users == session.list()
    session.roll_back()  # destroy all modifications
    session.close()
    conection.close()


