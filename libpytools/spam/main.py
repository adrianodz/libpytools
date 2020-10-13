class SpamSender:
    def __init__(self, session, sender):
        self.session = session
        self.sender = sender

    def send_email(self, to, subject, body):
        for user in self.session.list():
            self.sender.send(
                to,
                user.email,
                subject,
                body,
            )
