import socket,sys
from morpionBis_catcha import*


class Client:
    def __init__(self):
        self.HOST = socket.gethostname()
        self.PORT = 15000
        self.x = 0

        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connexion(self):
        try:
            self.mySocket.connect((self.HOST, self.PORT))
        except socket.error:
            print("La connexion a échoué.")
            sys.exit()
        print("Connexion établie avec le serveur.")

        msgServeur = self.mySocket.recv(1024).decode()
        print(msgServeur)

        while 1:
            if self.x == 0:
                if msgServeur.upper() == "FIN" or msgServeur == "":
                    break
                code = partie()
                if code == "0":
                    print("c'est finis")
                    break
                self.mySocket.send(code.encode())
                msgServeur = self.mySocket.recv(1024).decode()
                self.x += 1
            else:
                if msgServeur.upper() == "FIN" or msgServeur == "":
                    break
                code = partie(msgServeur)
                if code == "0":
                    print(code)
                    break
                self.mySocket.send(code.encode())
                msgServeur = self.mySocket.recv(1024).decode()

        print("Connexion interrompue.")
        self.mySocket.close()

