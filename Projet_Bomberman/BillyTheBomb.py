from tkinter import *
from tkinter.messagebox import *
from random import *
import time
from threading import *
import Decor
import Joueur


if __name__=="__main__":
        Joueur.Fenêtre = Tk()
        Decor.initialisation_incassables(10)
        Couleur = "grey"
        Zone = Canvas(Joueur.Fenêtre, width=Decor.Largeur, height=Decor.Hauteur, background=Couleur)
        grille = Decor.grille(Zone, 2, 'black')
        Decor.dessine_incassables(Zone)
        Joueur.Player = Joueur.Personnage(Zone, 'grey')
        Joueur.Player2 = Joueur.Personnage2(Zone, 'blue')
        #grille(2, "black")
        #bombe = Bombe(Zone, Joueur)
        Joueur.Fenêtre.mainloop()

        

