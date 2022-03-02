from unittest.mock import Mock

from libpythonpro import github_api


def teste_buscar_avatar():
    resp_mock = Mock()
    resp_mock.json.return_value = {
        'login': 'aislansantos', 'id': 53060089, 'node_id': 'MDQ6VXNlcjUzMDYwMDg5',
        'avatar_url': 'https://avatars.githubusercontent.com/u/53060089?v=4'
    }
    github_api.requests.get = Mock(return_value=resp_mock)
    url = github_api.buscar_avatar('aislansantos')
    assert 'https://avatars.githubusercontent.com/u/53060089?v=4' == url
