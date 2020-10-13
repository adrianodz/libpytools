from unittest.mock import Mock

import pytest

from libpytools.spam.main import SpamSender


# def test_send_spam(session):
#     spam_sender = SpamSender(session, Sender())
#     spam_sender.send_email(
#         'adriano@adriano.com',
#         'Subject',
#         'email body teste...',
#
from libpytools.spam.models import User


@pytest.mark.parametrize(
    'users',
    [
        [
            User(name='Adriano', email='adriano@adriano.com'),
            User(name='Luciano', email='luciano@luciano.com'),
        ],
        [
            User(name='Luciano', email='luciano@luciano.com'),
        ]
    ]
)
def test_amount_spam(session, users):
    for user in users:
        session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_email(
        'adriano@adriano.com',
        'Subject',
        'email body teste...',
    )
    assert len(users) == sender.send.call_count


# class SenderMock(Sender):
#     def __init__(self):
#         super().__init__()
#         self.amount_sent_email = 0
#         self.send_parameters = None
#
#     def send(self, from_name, to_name, subject, body):
#         self.send_parameters = (from_name, to_name, subject, body)
#         self.amount_sent_email += 1

def test_parameters_spam(session):
    user = User(name='Adriano', email='adriano@adriano.com')
    session.save(user)
    sender = Mock()
    spam_sender = SpamSender(session, sender)
    spam_sender.send_email(
        'luciano@luciano.com',
        'Subject',
        'email body teste...',
    )
    sender.send.assert_called_once_with(
        'luciano@luciano.com',
        'adriano@adriano.com',
        'Subject',
        'email body teste...',
    )
