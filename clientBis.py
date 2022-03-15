
import socket,sys
from morpionBis_catcha import*


"ip de mon pc = '192.168.1.94'"
HOST = socket.gethostname()
PORT = 15000
x = 0

mySocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

try:
    mySocket.connect((HOST, PORT))
except socket.error:
    print("La connexion a échoué.")
    sys.exit()
print("Connexion établie avec le serveur.")

# 3) Dialogue avec le serveur :
msgServeur = mySocket.recv(1024).decode()

while 1:
    if x == 0:
        if msgServeur.upper() == "FIN" or msgServeur =="":
            break
        code = partie()
        if code == "0":
            print("c'est finis")
            break
        mySocket.send(code.encode())
        msgServeur = mySocket.recv(1024).decode()
        x += 1
    else:
        if msgServeur.upper() == "FIN" or msgServeur =="":
            break
        code = partie(msgServeur)
        if code == "0":
            print(code)
            break
        mySocket.send(code.encode())
        msgServeur = mySocket.recv(1024).decode()


print("Connexion interrompue.")
mySocket.close()
