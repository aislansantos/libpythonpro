class Enviador:
    def enviar(self, remetente, destinatario, assunto, corpo):
        if '@' not in remetente:
            raise Emailnvalido(f'E-mail de rementente inválido: {remetente}')
        return remetente


class Emailnvalido(Exception):
    pass
