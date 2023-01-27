import socket
import threading

class Client_Socket:

    def __init__(self, host: str, port: int):
        self._host = host
        self._port = port
        self._endereco = (host, port)
        self._client:socket
        self._conexao_status = False
        self._callback_ao_dados = lambda dados: print(f"Ainda não implementado callback de dado {dados}")
        self._callback_conexao_status_mudou = lambda status: print(f"Ainda não implementado callback conexão status {status}")
        threading.Thread(target=self.verifica_dados).start()

    def conecta_socket(self):
        try:
            if not self._conexao_status:

                self._client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                self._client.connect(self._endereco)
                self._set_conexao_status(True)

        except Exception:

            self._set_conexao_status(False)


    def verifica_dados(self):
        while True:
            if self._conexao_status:
                dado = self._client.recv(1024).decode("UTF-8")
                print(dado)
                if dado:
                    self._callback_ao_dados(dado)
                    continue

                self.fechar_conexao()

    def enviar_dados(self, dado):
        if self._conexao_status:
            try:
                self._client.send(str.encode(dado))
            except Exception:
                self.fechar_conexao()

    def fechar_conexao(self):
        if self._conexao_status:
            self._client.shutdown(2)
            self._client.close()
            self._set_conexao_status(False)

    @property
    def callback_ao_dados(self):
        return self._callback_ao_dados and True

    @callback_ao_dados.setter
    def callback_ao_dados(self, callbak):
        self._callback_ao_dados = callbak

    @property
    def callback_conexao_status_mudou(self):
        return self._callback_conexao_status_mudou and True

    @callback_ao_dados.setter
    def callback_conexao_status_mudou(self, callbak):
        self._callback_conexao_status_mudou = callbak

    @property
    def conexao_status(self):
        return self._conexao_status

    def _set_conexao_status(self, valor):
        self._callback_conexao_status_mudou(valor)
        self._conexao_status = valor
