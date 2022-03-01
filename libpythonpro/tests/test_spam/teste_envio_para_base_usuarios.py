import pytest

from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadoDeSpam
from libpythonpro.spam.modelos import Usuario


class EnviadorMock(Enviador):

    def __init__(self):
        super().__init__()
        self.qtd_email_enviados = 0
        self.parametros_de_envio = None

    def enviar(self, remetente, destinatario, assunto, corpo):
        self.parametros_de_envio = (remetente, destinatario, assunto, corpo)
        self.qtd_email_enviados += 1


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
    enviador = EnviadorMock()
    enviador_de_spam = EnviadoDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'aislan.santos@gmail.com',
        'Curso PythonPro',
        'Confira os módulos fantásticos'
    )
    assert len(usuarios) == enviador.qtd_email_enviados


def test_parametros_de_spam(sessao):
    usuario = Usuario(nome='Aislan', email='aislan.santos@gmail.com')
    sessao.salvar(usuario)
    enviador = EnviadorMock()
    enviador_de_spam = EnviadoDeSpam(sessao, enviador)
    enviador_de_spam.enviar_email(
        'augusto.santos@gmail.com',
        'Curso PythonPro',
        'Confira os módulos fantásticos'
    )
    assert enviador.parametros_de_envio == (
        'augusto.santos@gmail.com',
        'aislan.santos@gmail.com',
        'Curso PythonPro',
        'Confira os módulos fantásticos'
    )
