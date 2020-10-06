from libpytools.spam.email_sender import Sender
from libpytools.spam.main import SpamSender


def test_send_spam(session):
    spam_sender = SpamSender(session, Sender())
    spam_sender.send_email(
        'adriano@adriano.com',
        'Subject',
        'email body teste...',
    )
