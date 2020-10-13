import requests


def find_avatar(user):
    """
    Find the avatar's Github from a user
    :param user: str with the name to find
    :return: str with the link to the avatar's Github
    """

    url = f'https://api.github.com/users/{user}'
    resp = requests.get(url)
    return resp.json()['avatar_url']
