import random
import socket
import threading
import tkinter as ttk

import select

if __name__ == '__main__':

    def enviar_identificador():

        id = entrada_id.get()
        modelo = entrada_modelo.get()

        enviarData(f"{id}:{modelo}")

    def enviar_dado():

        id_periferico = entrada_id_periferico.get()
        nome = entrada_nome.get()
        data = entrada_data.get()
        contexto = entrada_contexto.get()
        dado = entrada_dado.get()

        enviarData(f"IDP:{id_periferico},NM:{nome},DD:{dado},DT:{data},CT:{contexto};")

    def gerar_dado_aleatorio():
        entrada_dado.delete(0, ttk.END)
        entrada_dado.insert(0, f"{random.random()}")

    # Criando socket client

    HOST = '127.0.0.1'
    PORT = 8080

    conectado = False

    def conectar():

        global conectado
        global client

        try:
            if not conectado:
                client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
                client.connect((HOST, PORT))
                status_client["text"] = "Conectado"
                conectado = True

        except ValueError:

            status_client["text"] = "Desconectado"
            conectado = False


    def onData():

        global conectado

        while True:
            if conectado:

                try:
                    data = client.recv(1024)

                    if not data:
                        client.shutdown(2)
                        client.close()
                        status_client["text"] = "Desconectado"
                        conectado = False

                    if data:
                        mensagem_recebida["text"] = data.decode("UTF-8")

                except ValueError:
                    client.shutdown(2)
                    client.close()
                    status_client["text"] = "Desconectado"
                    conectado = False


    def enviarData(dado):

        global conectado

        if conectado:
            client.sendall(str.encode(dado))

    def desconectar():

        global conectado

        if conectado:
            client.close()

    threading.Thread(target=onData).start()

    app = ttk.Tk()
    app.title("Client tester")

    LARGURA = 500
    ALTURA = 300

    TELAX = app.winfo_screenwidth()
    TELAY = app.winfo_screenheight()

    POSX = int(TELAX/2 - LARGURA/2)
    POSY = int(TELAY/2 - ALTURA/2) - 50

    app.geometry(f"{LARGURA}x{ALTURA}+{POSX}+{POSY}")

    ###

    mensagem_recebida = ttk.Label(app, text="---")
    mensagem_recebida.grid(column=0, row=0, columnspan=4)

    ###

    botao_conectar = ttk.Button(app,
                                text="Conectar",
                                command=conectar)
    botao_conectar.grid(column=0, row=1)

    status_client = ttk.Label(app, text="Desconectado")
    status_client.grid(column=1, row=1, columnspan=3)

    ###

    botao_id_modelo = ttk.Button(app,
                                 text="Enviar Identificador",
                                 command=enviar_identificador)
    botao_id_modelo.grid(column=0, row=2, rowspan=2)

    ttk.Label(app, text="ID").grid(column=1, row=2)
    entrada_id = ttk.Entry(app)
    entrada_id.grid(column=1, row=3)

    ttk.Label(app, text="MODELO").grid(column=3, row=2)
    entrada_modelo = ttk.Entry(app)
    entrada_modelo.grid(column=3, row=3)

    ###

    botao_enviar_dado = ttk.Button(app,
                                   text="Enviar Dado",
                                   command=enviar_dado)
    botao_enviar_dado.grid(column=0, row=4, rowspan=4)

    ttk.Label(app, text="ID PERIFERICO").grid(column=1, row=4)
    entrada_id_periferico = ttk.Entry(app)
    entrada_id_periferico.grid(column=1, row=5)

    ttk.Label(app, text="NOME").grid(column=2, row=4)
    entrada_nome = ttk.Entry(app)
    entrada_nome.grid(column=2, row=5)

    ttk.Label(app, text="DATA").grid(column=3, row=4)
    entrada_data = ttk.Entry(app)
    entrada_data.grid(column=3, row=5)

    ttk.Label(app, text="CONTEXTO").grid(column=1, row=6)
    entrada_contexto = ttk.Entry(app)
    entrada_contexto.grid(column=1, row=7)

    ttk.Label(app, text="DADO").grid(column=2, row=6)
    entrada_dado = ttk.Entry(app)
    entrada_dado.grid(column=2, row=7)

    botao_gerar_dado = ttk.Button(app, text="Gerar dado Aleatorio", command=gerar_dado_aleatorio)
    botao_gerar_dado.grid(column=3, row=6, rowspan=2)

    app.mainloop()