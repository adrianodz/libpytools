from libpytools.spam.models import User


def test_save_user(session):
    user = User(name='Adriano')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_user(session):
    users = [User(name='Adriano'), User(name='Luciano')]
    for user in users:
        session.save(user)
    assert users == session.list()
