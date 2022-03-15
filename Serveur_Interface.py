from tkinter import*
from serveurTest import *
from clientTest import *

screen = Tk()
screen.title("Morpion")


def runn():
    b = Serveur()
    b.connexion()


bu = Button(text="Serveur", command=runn)
bu.pack()

screen.mainloop()
