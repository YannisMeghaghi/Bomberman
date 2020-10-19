from tkinter import *
from tkinter.messagebox import *
from random import *
import time
from threading import *

Largeur = 600
Hauteur = 600
largeur_case = Largeur//10
hauteur_case = Hauteur//10
incassables = []

def grille(zone, epaisseur, couleur):
        for i in range(9):
                zone.create_line(0, hauteur_case*(i+1), Largeur, hauteur_case*(i+1), fill=couleur, width=epaisseur)
        for j in range(9):
                zone.create_line(largeur_case*(j+1), 0, largeur_case*(j+1), Hauteur, fill=couleur, width=epaisseur)
        zone.pack()
        
def initialisation_incassables(nombre):
        global incassables
        incassables = []
        for i in range(nombre):
                incassables.append([randint(0, 9),randint(0, 9)])
                
def dessine_incassables(zone):
        for position in incassables: 
                zone.create_rectangle(position[0]*hauteur_case, position[1]*hauteur_case, position[0]*largeur_case + 60, position[1]*largeur_case + 60, fill='black')
                #zone.create_rectangle(position[0]*largeur_case, position[1]*hauteur_case, position[0]*largeur_case + 60, position[1]*largeur_case + 60)


def recherche_incassable(position):
        for pos in incassables:    # pos = couple de coordonnées, position aussi. 
                if pos == position: # regarde si le couple de coordonnées est égale à aux couples dans incassables
                        return True # retourne oui si c'est égale
        return False #sinon retourne faux


if __name__=="__main__":
        initialisation_incassables(20)
        Fenêtre = Tk()
        Couleur = 'white'
        Zone = Canvas(Fenêtre, width=Largeur, height=Hauteur, background=Couleur)
        dessine_incassables(Zone)
        grille(Zone, 2, "black")
