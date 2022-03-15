import socket, sys
from morpioninter import*

HOST = socket.gethostname()
PORT = 15000

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.bind((HOST, PORT))
except socket.error:
    print("La liaison du socket à l'adresse choisie a échoué.")
    sys.exit()

while 1:
    print("Serveur prêt, en attente de requêtes ...")
    mySocket.listen(5)

    connexion, adresse = mySocket.accept()
    print("Client connecté, adresse IP %s, port %s" % (adresse[0], adresse[1]))

    connexion.send("Serveur du Morpion".encode())
    msgClient = connexion.recv(1024).decode()
    while 1:
        if msgClient.upper() == "FIN" or msgClient =="":
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
    if ch.upper() =='T':
        break

