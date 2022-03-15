from tkinter import *
import socket,sys
from random import *
#from morpionBis_catcha import *
#from clientTest import *

screen = Tk()
screen.title("Client")
screen.geometry("200x200")

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


class morpion:
    def __init__(self):
        self.grille = [["#","#","#"],["#","#","#"],["#","#","#"]]
        self.save = [["#","#","#"],["#","#","#"],["#","#","#"]]
        self.soluce = {
        1:["#","#","#"],
        2:["O","#","#"],3:["#","O","#"],4:["#","#","O"],
        5:["O","O","#"],6:["O","#","O"],7:["#","O","O"],
        8:["O","O","O"],
        9:["X","#","#"],10:["#","X","#"],11:["#","#","X"],
        12:["X","X","#"],13:["X","#","X"],14:["#","X","X"],
        15:["X","X","X"],
        16:["O","X","#"],17:["O","#","X"],18:["O","X","X"],
        19:["X","O","#"],21:["X","O","O"],
        22:["X","O","X"],23:["O","X","O"],
        24:["#","X","O"],25:["X","#","O"],26:["X","X","O"],
        27:["#","O","X"],29:["O","O","X"]
        }
        assert type(self.grille) == list and self.save == [["#","#","#"],["#","#","#"],["#","#","#"]] and self.soluce == {1:["#","#","#"],2:["O","#","#"],3:["#","O","#"],4:["#","#","O"],5:["O","O","#"],6:["O","#","O"],7:["#","O","O"],8:["O","O","O"],9:["X","#","#"],10:["#","X","#"],11:["#","#","X"],12:["X","X","#"],13:["X","#","X"],14:["#","X","X"],15:["X","X","X"],16:["O","X","#"],17:["O","#","X"],18:["O","X","X"],19:["X","O","#"],21:["X","O","O"],22:["X","O","X"],23:["O","X","O"],24:["#","X","O"],25:["X","#","O"],26:["X","X","O"],27:["#","O","X"],29:["O","O","X"]}, "les données du morpion sont corrompue"

    def affiche(self):
        txt = f"{self.grille[0][:3]}\n{self.grille[1][:3]}\n{self.grille[2][:3]}"

        text = Label(text=txt)
        screen.update()
        text.pack()

    def ajoute(self,c,l,XorO):
        """Cette méthode prend des info : colonne ligne et X ou O puis modifie la grille de morpion en fonction"""
        assert type(self.grille) == list , " la grille n'est pas une liste"
        assert type(self.grille) == list and self.save ==  [["#","#","#"],["#","#","#"],["#","#","#"]] and self.soluce == {1:["#","#","#"],2:["O","#","#"],3:["#","O","#"],4:["#","#","O"],5:["O","O","#"],6:["O","#","O"],7:["#","O","O"],8:["O","O","O"],9:["X","#","#"],10:["#","X","#"],11:["#","#","X"],12:["X","X","#"],13:["X","#","X"],14:["#","X","X"],15:["X","X","X"],16:["O","X","#"],17:["O","#","X"],18:["O","X","X"],19:["X","O","#"],21:["X","O","O"],22:["X","O","X"],23:["O","X","O"],24:["#","X","O"],25:["X","#","O"],26:["X","X","O"],27:["#","O","X"],29:["O","O","X"]}, "les données du morpion sont corrompue"
        assert type(self.grille[0]) == list and type(self.grille[1]) == list and type(self.grille[2]) == list , "la grille est corrompue"
        if XorO == "O":
            if c == 1:
                if l == 1:
                    self.grille[0][0] = "O"
                elif l == 2:
                    self.grille[1][0] = "O"
                elif l == 3:
                    self.grille[2][0] = "O"
            elif c == 2:
                if l == 1:
                    self.grille[0][1] = "O"
                elif l == 2:
                    self.grille[1][1] = "O"
                elif l == 3:
                    self.grille[2][1] = "O"
            elif c == 3:
                if l == 1:
                    self.grille[0][2] = "O"
                elif l == 2:
                    self.grille[1][2] = "O"
                elif l == 3:
                    self.grille[2][2] = "O"
        elif XorO == "X":
            if c == 1:
                if l == 1:
                    self.grille[0][0] = "X"
                elif l == 2:
                    self.grille[1][0] = "X"
                elif l == 3:
                    self.grille[2][0] = "X"
            elif c == 2:
                if l == 1:
                    self.grille[0][1] = "X"
                elif l == 2:
                    self.grille[1][1] = "X"
                elif l == 3:
                    self.grille[2][1] = "X"
            elif c == 3:
                if l == 1:
                    self.grille[0][2] = "X"
                elif l == 2:
                    self.grille[1][2] = "X"
                elif l == 3:
                    self.grille[2][2] = "X"

    def reset(self):
        self.grille = self.save


def tourDeJeu(x,c,l, *cle):
    """Cette fonction prend des arguments et lance un tour de morpion puis renvoi un code qui correspond a la grile actuelle"""
    g = morpion()
    arg = '1/1/1/'
    for arg in cle:
        assert type(arg) == str,"la cle est pas une cle"
        g.grille = transfo(arg)
    if g.grille != 0:

        g.grille[int(l)-1][int(c)-1] = x
        code = codage(g.grille)
        y = transfo(code)
        if l == "1":
            y[1] = transfo(arg)[1]
            y[2] = transfo(arg)[2]
        elif l == "2":
            y[0] = transfo(arg)[0]
            y[2] = transfo(arg)[2]
        elif l == "3":
            y[0] = transfo(arg)[0]
            y[1] = transfo(arg)[1]
        code = codage(y)
        g.grille = y
        assert type(code) == str, "Le code est pas un texte"
        return code


def partie(*parametre):
    pp = 0
    bool = False
    p = None
    for arg in parametre:
        p = arg
    Grille = morpion()
    if p == None:
        Grille.affiche()
    else:
        Grille.grille = transfo(p)
        Grille.affiche()
        fichier = open('combinaison_gagnant.txt', 'r')
        contenu = fichier.readlines()

        grillon = codage(Grille.grille).split("/")
        grillon.remove(grillon[-1])
        """TEST"""
        texte = ""
        texte = texte + str(grillon) + "\n"
        for i in range(len(contenu)):
            if texte == contenu[i] and pp == 0:
                bool = True
                pp += 1

        if bool:
            return "0"

    x = input("Que voulez vous jouez ? <X> ou <O> :")
    l = input("quelle ligne: ")
    c = input("quelle colonne: ")
    if p == None:
        code = tourDeJeu(x, c, l)
    else:
        code = tourDeJeu(x, c, l, p)
    Grille.grille = transfo(code)
    Grille.affiche()

    fichier = open('combinaison_gagnant.txt', 'r')
    contenu = fichier.readlines()
    grillon = codage(Grille.grille).split("/")
    grillon.remove(grillon[-1])

    """TEST"""
    texte = ""
    texte = texte + str(grillon) + "\n"
    for i in range(len(contenu)):
        if texte == contenu[i] and pp == 0:
            bool = True
            pp += 1

    if bool:
        return "0"

    assert type(code) == str, "le code n'est pas un texte"
    assert len(code) < 11, "le code est trop long"
    return code


def transfo(code:str)->list:
    """cette fonction change le code en une liste"""
    assert type(code) == str,"le code n'est pas un string, transfo"
    g = morpion()
    cooode = 1
    grile = code.split("/")
    grile.remove(grile[-1])
    for i in range(3):
        for key,gri in g.soluce.items():
            if int(key) == int(grile[i]):
                cooode = key
        g.grille[i] = g.soluce[cooode]
        cooode = 1
    assert type(g.grille) == list, "Transfo ne renvoi pas une liste"
    return g.grille


def codage(grille: list) -> str:
    """cette fonction transforme le morpion en un code"""
    assert type(grille) == list , "la grille n'est pas une liste,codage"
    code = ""
    h = morpion()
    for i in range(3):
        for key,gri in h.soluce.items():
            if gri == grille[i]:
                code = code + str(key) + "/"
    assert type(code) == str,"le code nes pas un texte, codage"
    return code







#catcha

def a_gagner(code):
    chaine = code.split("/")
    chaine.remove(chaine[-1])
    return chaine


def rechercheBis(liste,element):
    texte = ""
    texte = texte + str(element) + "\n"
    for i in range(len(liste)):
        if texte == liste[i]:
            return True
        else:
            return False

def catcha():
    m = morpion()
    grille = []
    for i in range(3):
        r = randint(1, 29)
        if r == 20:
            r -= 1
        if r == 28:
            r -=1
        grille.append(m.soluce[r])
    m.grille = grille
    m.affiche()
    reponse = input("Y a t'il un gagnant ? <O>oui ou <N>non : ")
    if reponse.upper() == "O":
        fichier = open('combinaison_gagnant.txt', 'r')
        contenu = fichier.readlines()
        grillon = codage(m.grille).split("/")
        grillon.remove(grillon[-1])
        print(rechercheBis(contenu, grillon))
        if rechercheBis(contenu, grillon) == False:
            fichier = open('combinaison_gagnant.txt', 'a')
            fichier.write(str(a_gagner(codage(m.grille))) + "\n")
            fichier.close()






def run():
    b = Client()
    b.connexion()


bu = Button(text="Client", command=run)
bu.pack()

screen.mainloop()
