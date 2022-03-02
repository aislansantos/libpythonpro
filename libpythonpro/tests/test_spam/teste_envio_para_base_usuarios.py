from unittest.mock import Mock
import pytest
from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadoDeSpam
from libpythonpro.spam.modelos import Usuario

'''
class EnviadorMock(Enviador):
    ---> Mock é quando trocamos um objeto por outro. temos uma biblioteca de Mock.
    Que esta dentro de unittest.mock import mock, ela é toda escrita em inglês
    E mesmo assim quando usando um mock.metodo_qualquer ela não da erro
    Ela grava como um metodo aconteceu depois pode-se fazer metodos de asserção
    perguntando como um metodo foi executado, esse metodo é importante pois com ele
    não temos a necessidade de fazer todo esse código do metodo EnviadorMock

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1
'''


@pytest.mark.parametrize(
    'usuarios',
    [
        [
            Usuario(nome='Aislan', email='aislan.santos@gmail.com'),
            Usuario(nome='Augusto', email='aislan.santos@gmail.com')
        ],
        [
            Usuario(nome='Aislan', email='aislan.santos@gmail.com')
        ]
    ]
)
def test_qde_de_spam(sessao, usuarios):
    for usuario in usuarios:
        sessao.salvar(usuario)
    # Criação do Mock
    enviador = Mock()
    enviador_de_spam = EnviadoDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'aislan.santos@gmail.com',
        'Curso PythonPro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.enviar.call_count  # Contamos quantas vezes o enviador foi chamado.


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Aislan', email='aislan.santos@gmail.com')
    sessao.salvar(usuario)
    enviador = Mock()
    enviador_de_spam = EnviadoDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'augusto.santos@gmail.com',
        'Curso PythonPro',
        'Confira os módulos fantásticos'
    )
    # Confirmando se o método enviar foi chamado apenas uma vez com os parametros a seguir
    enviador.enviar.assert_called_once_with(
        'augusto.santos@gmail.com',
        'aislan.santos@gmail.com',
        'Curso PythonPro',
        'Confira os módulos fantásticos'
    )
