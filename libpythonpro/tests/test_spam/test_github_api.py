from unittest.mock import Mock
import pytest
from pytest_mock import mocker

from libpythonpro import github_api


@pytest.fixture
def avatar_url(mocker):
    resp_mock = Mock()
    url = 'https://avatars.githubusercontent.com/u/53060089?v=4'
    resp_mock.json.return_value = {
        'login': 'aislansantos', 'id': 53060089, 'node_id': 'MDQ6VXNlcjUzMDYwMDg5',
        'avatar_url': url
    }
    get_mock = mocker.patch('libpythonpro.github_api.requests.get')
    get_mock.return_value = resp_mock
    return url


def teste_buscar_avatar(avatar_url):
    url = github_api.buscar_avatar('aislansantos')
    assert avatar_url == url


def teste_buscar_avatar_integracao():
    url = github_api.buscar_avatar('renzon')
    assert 'https://avatars.githubusercontent.com/u/3457115?v=4' == url
