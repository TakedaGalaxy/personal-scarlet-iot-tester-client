import tkinter as ttk
import random
from classes import socketC

class Interface_Client:

    def __init__(self, titulo: str, client: socketC.Client_Socket):

        self._client = client
        self._client.callback_ao_dados = self._mensagem_recebida
        self._client.callback_conexao_status_mudou = self._conexao_status_mudou

        self._app = ttk.Tk()
        self._app.title(titulo)

        LARGURA = 500
        ALTURA = 300

        TELAX = self._app.winfo_screenwidth()
        TELAY = self._app.winfo_screenheight()

        POSX = int(TELAX/2 - LARGURA/2)
        POSY = int(TELAY/2 - ALTURA/2) - 50

        self._app.geometry(f"{LARGURA}x{ALTURA}+{POSX}+{POSY}")

    def _mensagem_recebida(self, dado: str):
        self._mensagem_recebida_l["text"] = dado

    def _conexao_status_mudou(self, status: bool):
        print(status)
        self._status_client["text"] = "Conectado" if status else "Desconectado"

    def _conectar(self):
        self._client.conecta_socket()

    def _envia_identificador(self):
        id = self._entrada_id.get()
        modelo = self._entrada_modelo.get()

        self._client.enviar_dados(f"{id}:{modelo}")

    def _envia_dado(self):
        id_periferico = self._entrada_id_periferico.get()
        nome = self._entrada_nome.get()
        data = self._entrada_data.get()
        contexto = self._entrada_contexto.get()
        dado = self._entrada_dado.get()

        self._client.enviar_dados(f"IDP:{id_periferico},NM:{nome},DD:{dado},DT:{data},CT:{contexto};")

    def _gerar_dado_aleatorio(self):
        self._entrada_dado.delete(0, ttk.END)
        self._entrada_dado.insert(0, f"{random.random()}")

    def _criar_estrutura(self):

        self._mensagem_recebida_l = ttk.Label(self._app, text="")
        self._mensagem_recebida_l.grid(column=0, row=0, columnspan=4)

        ###

        botao_conectar = ttk.Button(self._app,
                                    text="Conectar",
                                    command=self._conectar)
        botao_conectar.grid(column=0, row=1)

        self._status_client = ttk.Label(self._app, text="Desconectado")
        self._status_client.grid(column=1, row=1, columnspan=3)

        ###

        botao_id_modelo = ttk.Button(self._app,
                                     text="Enviar Identificador",
                                     command=self._envia_identificador)
        botao_id_modelo.grid(column=0, row=2, rowspan=2)

        ttk.Label(self._app, text="ID").grid(column=1, row=2)
        self._entrada_id = ttk.Entry(self._app)
        self._entrada_id.grid(column=1, row=3)

        ttk.Label(self._app, text="MODELO").grid(column=3, row=2)
        self._entrada_modelo = ttk.Entry(self._app)
        self._entrada_modelo.grid(column=3, row=3)

        ###

        botao_enviar_dado = ttk.Button(self._app,
                                       text="Enviar Dado",
                                       command=self._envia_dado)
        botao_enviar_dado.grid(column=0, row=4, rowspan=4)

        ttk.Label(self._app, text="ID PERIFERICO").grid(column=1, row=4)
        self._entrada_id_periferico = ttk.Entry(self._app)
        self._entrada_id_periferico.grid(column=1, row=5)

        ttk.Label(self._app, text="NOME").grid(column=2, row=4)
        self._entrada_nome = ttk.Entry(self._app)
        self._entrada_nome.grid(column=2, row=5)

        ttk.Label(self._app, text="DATA").grid(column=3, row=4)
        self._entrada_data = ttk.Entry(self._app)
        self._entrada_data.grid(column=3, row=5)

        ttk.Label(self._app, text="CONTEXTO").grid(column=1, row=6)
        self._entrada_contexto = ttk.Entry(self._app)
        self._entrada_contexto.grid(column=1, row=7)

        ttk.Label(self._app, text="DADO").grid(column=2, row=6)
        self._entrada_dado = ttk.Entry(self._app)
        self._entrada_dado.grid(column=2, row=7)

        botao_gerar_dado = ttk.Button(self._app, text="Gerar dado Aleatorio", command=self._gerar_dado_aleatorio)
        botao_gerar_dado.grid(column=3, row=6, rowspan=2)

    def run(self):

        self._criar_estrutura()

        self._app.mainloop()
