class Sender:
    def send(self, from_name, to_name, subject, body):
        if '@' not in from_name:
            raise InvalidEmail(f'invalid sender email {from_name}')
        return from_name


class InvalidEmail(Exception):
    pass
