from libpythonpro.spam.enviador_de_email import Enviador
from libpythonpro.spam.main import EnviadoDeSpam


def test_envio_de_spam(sessao):
    enviador_de_spam = EnviadoDeSpam(sessao, Enviador())
    enviador_de_spam.enviar_email(
        'aislan.santos@gmail.com',
        'Curso PythonPro',
        'Confira os módulos fantásticos'
    )
