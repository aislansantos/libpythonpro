import pytest

from libpythonpro.spam.enviador_de_email import Enviador, Emailnvalido


def test_criar_enviador_de_email():
    enviador = Enviador()
    assert enviador is not None


@pytest.mark.parametrize('rementente',
                         ['aislan.santos@gmail.com', 'teste@teste.com.br'])
def test_remetente(rementente):
    enviador = Enviador()
    resultado = enviador.enviar(rementente,
                                'aislan_85@yahoo.com.br',
                                'Cursos PythonPro',
                                'Primeira turma Guido Von Rossum aberta.'
                                )
    assert rementente in resultado


@pytest.mark.parametrize('rementente',
                         ['', 'teste'])
def test_remetente_invalido(rementente):
    enviador = Enviador()
    with  pytest.raises(Emailnvalido):
        enviador.enviar(rementente,
                        'aislan_85@yahoo.com.br',
                        'Cursos PythonPro',
                        'Primeira turma Guido Von Rossum aberta.'
                        )
