import pytest

from libpytools.spam.email_sender import Sender, InvalidEmail


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
    # for sender_field in sender_fields
    result = sender.send(
        sender_field,
        'email2@email.com',
        'Python Course',
        'First time.',
    )
    assert sender_field in result


@pytest.mark.parametrize(
    'sender_field',
    ['', 'foo']
)
def test_invalid_sender(sender_field):
    sender = Sender()
    with pytest.raises(InvalidEmail):
        result = sender.send(
            sender_field,
            'email2@email.com',
            'Python Course',
            'First time.',
        )
