from classes.socketC import Client_Socket
from classes.interfaceC import Interface_Client

if __name__ == '__main__':

    client = Client_Socket(host="127.0.0.1", port=8080)

    interface = Interface_Client("Client tester", client)

    interface.run()
