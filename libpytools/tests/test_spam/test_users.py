from libpytools.spam.models import User


def test_save_user(session):
    user = User(name='Adriano', email='adriano@adriano.com')
    session.save(user)
    assert isinstance(user.id, int)


def test_list_user(session):
    users = [
        User(name='Adriano', email='adriano@adriano.com'),
        User(name='Luciano', email='luciano@luciano.com'),
    ]
    for user in users:
        session.save(user)
    assert users == session.list()
