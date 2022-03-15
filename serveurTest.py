import socket, sys
from morpioninter import*


class Serveur:
    def __init__(self):
        self.HOST = socket.gethostname()
        self.PORT = 15000

        self.mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    def connexion(self):
        try:
            self.mySocket.bind((self.HOST, self.PORT))
        except socket.error:
            print("La liaison du socket à l'adresse choisie a échoué.")
            sys.exit()

        while 1:
            print("Serveur prêt, en attente de requêtes ...")
            self.mySocket.listen(5)

            connexion, adresse = self.mySocket.accept()
            print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))

            connexion.send("Serveur du Morpion".encode())
            msgClient = connexion.recv(1024).decode()
            while 1:
                if msgClient.upper() == "FIN" or msgClient == "":
                    break

                code = partie(msgClient)
                if code == "0":
                    print("c'est finis")
                    break
                connexion.send(code.encode())
                msgClient = connexion.recv(1024).decode()

            connexion.send("Au revoir !".encode())
            print("Connexion interrompue.")
            connexion.close()

            ch = input("<R>ecommencer <T>erminer ? ")
            if ch.upper() == 'T':
                break
