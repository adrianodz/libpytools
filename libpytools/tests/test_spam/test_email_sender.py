import pytest

from libpytools.spam.email_sender import Sender


def test_email_sender():
    sender = Sender()
    assert sender is not None

@pytest.mark.parametrize(
    'sender_field',
    ['email1@email.com', 'foo@bar.com']
)
def test_sender(sender_field):
    sender = Sender()
    # sender_fields = ['email1@email.com', 'foo@bar.com']
    result = sender.send(
        sender_field,
        'email2@email.com',
        'Python Course',
        'First time.',
    )
    assert sender_field in result