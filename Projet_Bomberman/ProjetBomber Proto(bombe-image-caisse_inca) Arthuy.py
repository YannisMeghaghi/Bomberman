from tkinter import *
from tkinter.messagebox import *
from random import *
import time
from threading import *

Largeur = 600
Hauteur = 600
largeur_case = Largeur//10
hauteur_case = Hauteur//10
Liste_des_bombes = []
incassables = []
Pos_joueur1 = [0,0]
Pos_joueur2 = [9,9]


def grille(epaisseur, couleur):
        global Zone
        for i in range(9):
                Zone.create_line(0, hauteur_case*(i+1), Largeur, hauteur_case*(i+1), fill=couleur, width=epaisseur)
        for j in range(9):
                Zone.create_line(largeur_case*(j+1), 0, largeur_case*(j+1), Hauteur, fill=couleur, width=epaisseur)
        Zone.pack()

def initialisation_incassables(nombre):                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                      
        global incassables
        for i in range(nombre):
                incassables.append([randint(0, 9),randint(0, 9)])
                
def dessine_incassables(zone):
        for position in incassables:
                #photo = PhotoImage(file ='bloc incassable')
                #zone.create_image(position[0]*largeur_case, position[1]*hauteur_case, image= photo)
                zone.create_rectangle(position[0]*largeur_case, position[1]*hauteur_case, position[0]*largeur_case + 60, position[1]*largeur_case + 60, fill='black')
                #self.photo = PhotoImage(file ='bloc incassable.GIF')                                                                                      
                #zone.create_rectangle(3, 3, largeur_case-3, hauteur_case-3)                                 

def recherche_incassable(position):
        for pos in incassables:    # pos = couple de coordonnées, position aussi. 
                if pos == position: # regarde si le couple de coordonnées est égale à aux couples dans incassables
                        return True # retourne oui si c'est égale
        return False #sinon retourne faux

class perpetualTimer():

   def __init__(self,t,hFunction):
      self.t=t
      self.hFunction = hFunction
      self.thread = Timer(self.t,self.handle_function)

   def handle_function(self):
      self.hFunction()
      self.thread = Timer(self.t,self.handle_function)
      self.thread.start()

   def start(self):
      self.thread.start()

   def cancel(self):
      self.thread.cancel()

class Bombe :
    def __init__(self, canvas, personnage):
                self.case = (personnage.case[0],personnage.case[1])
                self.canvas = canvas
                self.photo = PhotoImage(file ='Bombe Bomberman.gif')
                self.id = canvas.create_image(30, 30, image=self.photo)
                self.compteur = Timer(5, self.explode)
##                while compteur != 1:
##                        time.sleep(3.0)
##                        compteur =+ 1
                self.canvas.move(self.id, self.case[0]*largeur_case, self.case[1]*hauteur_case)
##                self.case = (0,0)
##                self.case = list(self.case)
##                self.temeps_de_vie = 100

    def explode(self): # Pour effacer le canvas de la bombe
                self.canvas.delete(self.id)
                print("explosion")
                if self.touche_un_joueur1() or self.touche_un_joueur2():
                        print("fin de partie")

    def touche_un_joueur1(self):
                global Pos_joueur1
                print(Pos_joueur1)                
                x_bombe = self.case[0]
                y_bombe = self.case[1]
                x_joueur = Pos_joueur1[0]
                y_joueur = Pos_joueur1[1]
                print(x_bombe, y_bombe)
                if y_bombe == y_joueur and x_joueur >= x_bombe - 1 and x_joueur <= x_bombe +1 or x_bombe == x_joueur and y_joueur >= y_bombe - 1 and y_joueur <= y_bombe +1:
                        print("condition_oui", x_bombe, y_bombe, Pos_joueur1)
                        return 1
                else:
                        print("condition_non", x_bombe, y_bombe, Pos_joueur1)
                        return 0
                    
    def touche_un_joueur2(self):
                x_bombe = self.case[0]
                y_bombe = self.case[1]
                x_joueur2 = Pos_joueur2[0]
                y_joueur2 = Pos_joueur2[1]
                if x_bombe + 1 == x_joueur2 or x_bombe -1 == x_joueur2 or y_bombe +1 == y_joueur2 or y_bombe -1 == y_joueur2 :
                        print("condition_oui2", x_bombe, y_bombe, Pos_joueur1)
                        return 1
                else:
                        print("condition_non2", x_bombe, y_bombe, Pos_joueur1)
                        return 0

        
        
class Personnage:
        def __init__(self, canvas, color):
                self.canvas = canvas
                self.photo = PhotoImage(file ='Bomberman_p1.gif')
                self.id = self.canvas.create_image(30, 30, image=self.photo)
                self.case = (0,0)
                self.case = list(self.case)
                #self.canvas.move(self.id, 200, 300)
                self.x = largeur_case
                self.y = hauteur_case
                self.canvas_width = self.canvas.winfo_width()
                self.canvas.bind_all('<KeyPress-q>', self.turn_left)
                self.canvas.bind_all('<KeyPress-d>', self.turn_right)
                self.canvas.bind_all('<KeyPress-z>', self.turn_up)
                self.canvas.bind_all('<KeyPress-s>', self.turn_down)
                self.canvas.bind_all('<space>',self.pose_bombe)

        def change_image(self, sens):#definition d'une methode qui attribue a un sens pris par le joueur une valeur. cette valeur est stocké et change l'image du joueur lorsqu'il effectie l'action
                if sens == 0:
                        self.photo=PhotoImage(file='Bomberman_p1turnleft.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
                elif sens == 1:
                        self.photo=PhotoImage(file='Bomberman_p1.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
                elif sens == 2:
                        self.photo=PhotoImage(file='Bomberman_p1.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
                elif sens == 3:
                        self.photo=PhotoImage(file='Bomberman_p1.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
                        
        def pose_bombe(self, evt): # fonction de pose de la bombe
                global Liste_des_bombes
                bombe = Bombe(self.canvas, self) # On récupère le canvas de la classe Bombe
                Liste_des_bombes.append(bombe) # On ajoute bombe à la liste pour pouvoir travailler dessus plus tard
                bombe.compteur.start()
                # Appele la fonction qui efface la bombe
        
        def test_incassable(self, direction):
                if direction == -1:     #Si direction =-1
                        if recherche_incassable([self.case[0]-1, self.case[1]]): #recharche si la pos (self.case[0]-1, self.case[1]) se trouve dans incassables
                                return False #retourne faux si il est dedans
                        else :
                                return True #retourne vrai si il n'est pas dedans
                elif direction == 1:
                        
                        if recherche_incassable([self.case[0]+1, self.case[1]]):
                                return False
                        else :
                                return True
                elif direction == -2:
                        
                        if recherche_incassable([self.case[0], self.case[1]-1]):
                                return False
                        else :
                                return True
                elif direction == 2 :

                        if recherche_incassable([self.case[0], self.case[1]+1]):
                                return False
                        else :
                                return True
                else :
                        return True

        def turn_left(self, evt) :
                self.change_image(0)
                if self.case[0] != 0 and self.test_incassable(-1): #C'est ici où les vraix et faux sont importants. Exemple 1er cas: self.case[0] != 0 : Vrai ;et ;self.test_incassable(-1):Vrai alors turn s'applique à vrai (vrai = 1)
                        self.canvas.move(self.id, -self.x, 0) #Suite: 2e cas: les deux sont faux la fonction s'applique pas donc il s'arrete -- 3e cas : un des deux est faux alors fonction est false (car 'and'-- 1*0=0)
                        time.sleep(0.1)# cooldown dans le déplacement   
                        self.case[0]=self.case[0]-1
                        print(self.case)
                else: 
                        print('ok')     

        def turn_right (self, evt) :
                self.change_image(1)
                if self.case[0]!= 9 and self.test_incassable(1): # on définit ici 1 comme 'a droite' pou la méthode test_incassable ; -1 = a gauche ; -2 = en haut ; 2 = en bas
                        self.canvas.move(self.id, self.x, 0)
                        self.case[0] = self.case[0] + 1 
                        print(self.case)
                else: 
                        print('ok')
                

        def turn_up (self, evt) :
                self.change_image(2)
                if self.case[1]!= 0 and self.test_incassable(-2):
                        self.canvas.move(self.id, 0, -self.y)
                        self.case[1] = self.case[1] - 1 
                        print(self.case)
                else: 
                        print('ok')

        def turn_down (self, evt) :
                self.change_image(3)
                if self.case[1]!= 9 and self.test_incassable(2):
                        self.canvas.move(self.id, 0, self.y)
                        self.case[1] = self.case[1] + 1
                        print(self.case)
                else:
                        print('ok')

               

    
class Personnage2:
        def __init__(self, canvas, color):
                self.canvas = canvas
                self.photo = PhotoImage(file ='Bomberman_p2.GIF')
                self.id = canvas.create_image(30, 30, image=self.photo)
                self.case = (9,9)
                self.case = list(self.case)
                self.canvas.move(self.id, 9*largeur_case, 9*hauteur_case)
                self.x = largeur_case
                self.y = hauteur_case
                self.canvas_width = self.canvas.winfo_width()
                self.canvas.bind_all('<KeyPress-Left>', self.turn_left)
                self.canvas.bind_all('<KeyPress-Right>', self.turn_right)
                self.canvas.bind_all('<KeyPress-Up>', self.turn_up)
                self.canvas.bind_all('<KeyPress-Down>', self.turn_down)
                self.canvas.bind_all('<KeyPress-0>',self.pose_bombe)
        def change_image(self, sens):#liste des images pour les animations de personnages
                if sens == 0:
                        self.photo=PhotoImage(file='Bomberman_p2turnleft.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
                elif sens == 1:
                        self.photo=PhotoImage(file='Bomberman_p2.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
                elif sens == 2:
                        self.photo=PhotoImage(file='Bomberman_p2.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
                elif sens == 3:
                        self.photo=PhotoImage(file='Bomberman_p2.gif')
                        self.canvas.itemconfigure(self.id, image = self.photo)
        def decompte(self, t):
                 for i in range(t):
                        bombe.time 
                        print(i)

                
        def pose_bombe(self, evt): # fonction de pose de la bombe
                global Liste_des_bombes
                bombe = Bombe(self.canvas, self) # On récupère le canvas de la classe Bombe
                Liste_des_bombes.append(bombe) # On ajoute bombe à la liste pour pouvoir travailler dessus plus tard
                bombe.compteur.start()
                # Appele la fonction qui efface la bombe

        def test_incassable(self, direction):
                if direction == -1:     #Si direction =-1
                        if recherche_incassable([self.case[0]-1, self.case[1]]): #recharche si la pos (self.case[0]-1, self.case[1]) se trouve dans incassables
                                return False #retroune faux si il est dedans
                        else :
                                return True #retourne vrai si il n'est pas dedans
                elif direction == 1:
                        
                        if recherche_incassable([self.case[0]+1, self.case[1]]):
                                return False
                        else :
                                return True
                elif direction == -2:
                        
                        if recherche_incassable([self.case[0], self.case[1]-1]):
                                return False
                        else :
                                return True
                elif direction == 2 :

                        if recherche_incassable([self.case[0], self.case[1]+1]):
                                return False
                        else :
                                return True
                else :
                        return True

        def turn_left(self, evt) :
                self.change_image(0)
                if self.case[0] != 0 and self.test_incassable(-1):
                        self.canvas.move(self.id, -self.x, 0)
                        self.case[0]=self.case[0]-1
                        print(self.case)
                else :
                        print('ok')
                

        def turn_right (self, evt):
                self.change_image(1)
                if self.case[0]!= 9 and self.test_incassable(1):
                        self.canvas.move(self.id, self.x, 0)
                        self.case[0] = self.case[0] + 1 
                        print(self.case)
                else :
                        print('ok')


        def turn_up (self, evt):
                self.change_image(2)
                if self.case[1]!= 0 and self.test_incassable(-2):
                        self.canvas.move(self.id, 0, -self.y)
                        self.case[1] = self.case[1] - 1 
                        print(self.case)
                else :
                        print('ok')

        def turn_down (self, evt):
                self.change_image(3)
                if self.case[1]!= 9 and self.test_incassable(2):
                        self.canvas.move(self.id, 0, self.y)
                        self.case[1] = self.case[1] + 1 
                        print(self.case)
                else :
                        print('ok')


if __name__=="__main__":
        initialisation_incassables(12)
        Fenêtre = Tk()
        Couleur = "white"
        Zone = Canvas(Fenêtre, width=Largeur, height=Hauteur, background=Couleur)
        dessine_incassables(Zone)
        grille(2, "black")
        Joueur = Personnage(Zone, 'blue')
        Joueur2 = Personnage2(Zone, 'green')
        #bombe = Bombe(Zone, Joueur)
        Fenêtre.mainloop()
        

