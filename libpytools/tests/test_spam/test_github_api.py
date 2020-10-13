from unittest.mock import Mock

import pytest

from libpytools import github_api


@pytest.fixture
def avatar_url():
    resp_mock = Mock()
    v_ = 'https://avatars0.githubusercontent.com/u/71018202?v=4'
    resp_mock.json.return_value = {'login': 'adrianodz',
                                   'id': 71018202,
                                   'node_id': 'MDQ6VXNlcjcxMDE4MjAy',
                                   'avatar_url': v_}
    get_original = github_api.requests.get
    github_api.requests.get = Mock(return_value=resp_mock)
    yield v_
    github_api.requests.get = get_original


def test_find_avatar(avatar_url):
    # if use the API in integration test, it could exceed limit connections to the API
    # it also, depends on the internet, otherwise the test will fall
    # url = github_api.find_avatar('adrianodz')
    # assert 'https://avatars0.githubusercontent.com/u/71018202?v=4' == url

    # so, I will use a Mock and simulate the response
    url = github_api.find_avatar('adrianodz')
    assert avatar_url == url


def test_find_avatar_integrationtest():
    url = github_api.find_avatar('adrianodz')
    assert 'https://avatars0.githubusercontent.com/u/71018202?v=4' == url
