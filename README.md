# projet_Immeuble_coorpoation_terminal_2023
Ceci est un projet que nous avions réaliser en terminal en groupe de 3

# Notation

+ Réalisation pratique du projet : 4/5
    + Pas d'interpréteur valide mais un début

+ Bonnes pratiques de programmation : 4/5
    + interpreteur.py : aucune fonction, tout est dans le programme principal...

+ Communication : 4/5
    + interpreteur.py : pas de documentation.

+ Revue de projet : 4/5
    + TB mais pas de jeux de tests permettant de valider la démarche


# Immeuble_coorporation

 **Lundi 12/09 22**

 **Lohan :**
 
 ```Python

 def trace_triangle_iso(feutre, x,y):
    '''Trace un triangle (isocele) à l'aide du crayon feutre
 
    :: param ftr(Turtle)    :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur en pixel des côtés 
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.begin_fill()    
    feutre.goto(x+140,y)
    
    feutre.left(100)
    feutre.forward(70)
    
    feutre.left(100)
    feutre.forward(70)
    
    feutre.left(100)
    feutre.end_fill()
    feutre.hideturtle()
```

**Tanguy**

```Python

def trace_carre(feutre, cote):
    '''Trace un carré à l'aide du crayon feutre

    :: param ftr(Turtle)    :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur 
    :: return (None)        :: fonction sans retour
 
    '''
    feutre.begin_fill()
    for i in range(4):
        feutre.forward(cote)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()

def carre(cote, infos, coordonnees):
    '''Trace un carré à partir des infos et aux bonnees coordonnées
 
    :: param cote(int)                     :: la valeur en pixel des côtés
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_carre(feutre, cote)
 
    return feutre
```
**julien**

```Python
def trace_rectangle(feutre, larg, long):
    '''Trace rectangle à l'aide du crayon feutre
 
    :: param feutre(Turtle)    :: la référence de l'objet Turtle
    :: param rayon(int)     :: la valeur en pixel du rayon
    :: param angle(int)     :: l'angle à tracer (360 pour un cercle)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.begin_fill()
    for x in range(4):
        if x == 0 or x == 2 :
            feutre.forward(larg)
            feutre.left(90)
        if x == 1 or x == 3 :
            feutre.forward(long)
            feutre.left(90)



def rectangle(larg, long, infos):
    '''Trace un rectangle à partir des infos et aux bonnees coordonnées
 
    :: param rayon(int)                    :: la valeur en pixel du rayon
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    coord = infos ['coordonnees']
    x = coord[0]                  # ou x,y = coordonnees
    y = coord[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_rectangle(feutre, larg, long)


def dessiner_facade(informations:dict):
    facade = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    facade['écriture'] = 'blue'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 5
    etage = randint(1,5)
    rectangle(140, etage*80, facade)
 ```
**mercredi 14/09 22**

 **Lohan :**

 ```Python
 def trace_toit_arc(feutre):
    '''Trace un arc de cercle à l'aide du crayon feutre
 
    :: param ftr(Turtle)    :: la référence de l'objet Turtle
    :: param rayon(int)     :: la valeur en pixel du rayon
    :: param angle(int)     :: l'angle à tracer (360 pour un cercle)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.begin_fill()
    feutre.goto(x,y)
    feutre.circle(140,180)
    feutre.end_fill()
    feutre.hideturtle()

    def triangle_iso(infos, coordonnees):
    
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
    trace_triangle_iso()
```

J'ai ajouté mes fonctions à rue pour plus tard
 ```Python

from formes import trace_triangle_iso as tti
from formes import trace_toit_arc as tta
```

**julien**

```python

# Importation
 
from formes import triangle_equilateral
from formes import rectangle
from random import randint
# Fonction gestion des données
 
def determiner_immeuble(numero:int) -> dict:
    caracteristiques = {}
    caracteristiques['couleur_facade'] = 'red'
    caracteristiques['numero'] = numero
    caracteristiques['position'] = -300 + numero*(140+70)
    caracteristiques['etage'] = randint(2, 6)
    return caracteristiques
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations:dict):
    facade = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    facade['écriture'] = 'blue'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 5
    etage = informations['etage']
    rectangle(140, etage*80, facade, (informations['position'], 0))
 
def dessiner_porte(informations:dict):
    pass

def dessiner_toit():
    pass
def dessiner_immeuble(informations:dict):
    dessiner_facade(informations)
    dessiner_porte(informations)
    # à compléter avec d'autres fonctions pour le reste : toit, fenêtres...
 
# Programme principal
 


if __name__ == '__main__':

    for x in range(4):
        infos_immeuble = determiner_immeuble(x)
        dessiner_immeuble(infos_immeuble)
```
**Julien**

```python
def dessiner_porte(informations:dict):
    porte = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    porte['écriture'] = 'blue'
    porte['fond'] = informations['couleur_facade']
    porte['épaisseur'] = 5
    rectangle(20, 30, porte, (informations['position_m'] + 20 + 40*informations['position_p'], 0))

def couleur ():
    i = randint(1,10)
    if i == 1 :
        c = 'red'
    if i == 2 :
        c = 'blue'
    if i == 3 :
        c = 'yellow'
    if i == 4 :
        c = 'orange'
    if i == 5 :
        c = 'purple'
    if i == 6 :
        c = 'green'
    if i == 7 :
        c = 'pink'
    if i == 8 :
        c = 'black'
    if i == 9 :
        c = 'grey'
    if i == 10 :
        c = 'brown'
    return c
    
def determiner_immeuble(numero:int) -> dict:
    caracteristiques = {}
    caracteristiques['couleur_facade'] = couleur()
    caracteristiques['numero'] = numero
    caracteristiques['position_m'] = -300 + numero*(140+70)
    caracteristiques['position_p'] = randint(0,2)
    caracteristiques['etage'] = randint(2, 6)
    return caracteristiques
 
 def trace_rectangle(feutre, larg, long):
    '''Trace rectangle à l'aide du crayon feutre
 
    :: param feutre(Turtle)    :: la référence de l'objet Turtle
    :: param rayon(int)     :: la valeur en pixel du rayon
    :: param angle(int)     :: l'angle à tracer (360 pour un cercle)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.begin_fill()
    for x in range(4):
        if x == 0 or x == 2 :
            feutre.forward(larg)
            feutre.left(90)
        if x == 1 or x == 3 :
            feutre.forward(long)
            feutre.left(90)
    feutre.end_fill()
```
**Tanguy**
```Python
    def dessiner_fenetre(x, p):
    ''' Dessine un fenêtre à la position
    '''
    fenetre = {} # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    fenetre['écriture'] = 'blue'
    fenetre['fond'] = informations['couleur_fenêtres']
    fenetre['épaisseur'] = 5
    carre(30, fenetre, (15,30))

def dessiner_fenetres_etage(x):
    '''Dessine les fenêtres d'un étage
    '''
    pass

def dessiner_fenetres_immeuble(informations:dict)
    '''Dessine toutes les fenêtres de l'immeuble
    '''
    pass
```
**Jeudi 15 septembre**

**Julien:**

```Python

# Importation
 
from formes import triangle_equilateral
from formes import rectangle
from random import randint
# Fonction gestion des données

def couleur ():
    i = randint(1,10)
    if i == 1 :
        c = 'red'
    if i == 2 :
        c = 'blue'
    if i == 3 :
        c = 'yellow'
    if i == 4 :
        c = 'orange'
    if i == 5 :
        c = 'purple'
    if i == 6 :
        c = 'green'
    if i == 7 :
        c = 'pink'
    if i == 8 :
        c = 'black'
    if i == 9 :
        c = 'grey'
    if i == 10 :
        c = 'brown'
    return c
def determiner_immeuble(numero:int) -> dict:
    ''' stock tout les données nécessaire pour créer un immeuble'''
    caracteristiques = {}
    caracteristiques['couleur_facade'] = couleur()
    caracteristiques['couleur_porte'] = couleur()
    caracteristiques['couleur_toit'] = couleur()
    caracteristiques['numero'] = numero
    caracteristiques['position_m'] = -300 + numero*(140+70)
    caracteristiques['position_p'] = randint(0,2)
    caracteristiques['etage'] = randint(2, 6)
    return caracteristiques
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations:dict):
    '''créer la façade d'un immeuble'''
    facade = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    facade['écriture'] = 'blue'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 5
    etage = informations['etage']
    rectangle(140, etage*80, facade, (informations['position_m'], 0))
 
def dessiner_porte(informations:dict):
    '''créer la porte d'un immeuble'''
    porte = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    porte['écriture'] = 'blue'
    porte['fond'] = informations['couleur_porte']
    porte['épaisseur'] = 5
    rectangle(20, 30, porte, (informations['position_m'] + 20 + 40*informations['position_p'], 0))
    
    
def dessiner_fenetres():
    '''crer les fenetre d'un batiment'''
    pass

def dessiner_toit_arc():
    '''creer le toit d'un batiment'''
    pass

def dessiner_immeuble(informations:dict):
    
    dessiner_facade(informations)
    dessiner_porte(informations)
    # à compléter avec d'autres fonctions pour le reste : toit, fenêtres...
 
# Programme principal
 


if __name__ == '__main__':

    for x in range(4):
        infos_immeuble = determiner_immeuble(x)
        dessiner_immeuble(infos_immeuble)
```
je met ça dans rue.py, quand vous aurez terminé vos fonction mettez les au bonne endroit et si vous trouver que mes documentations sont trop légère, changez les.    
N'oubliez pas d'utiliser la cle 'couleur_porte' pour la couleur alétoire du toit    
Et dernière chose faudrait se coordonnés pour les noms de fonction.      
je propose:       
_tanguy: t'a fonction dessiner_fenetres_immeuble en dessiner_fenetre ( je trouve que c'est mieux pour le programme rue.py)            
_ Lohan: def dessiner_toit dans rue.py si tu trouve l'idée bonne tu pourrai utiliser un chiffre aléatoire 1 ou 2 
, 1 pour un toit en triangle et 2 pour un toit en arc de cercle ( au moin ça fera une seul fonction pour chaque partie de l'immeuble dans le programme rue.py)      

**mercredi 21/09 22**

 **Lohan :**
 
 ```Python

 def triangle_iso(infos, coordonnees):
     '''Trace un triangle (isocele) à partir des infos et au bonnes coordonnées

    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)r

   '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
    
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_triangle_iso(feutre, x, y)

    ```

 **vendredi 23/09/22**

 **Tanguy : **

```Python
 def dessiner_fenetre() -> None:
    '''Dessine un fenêtre'''
    fenêtre = {}
    fenêtre['écriture'] = 'brown'
    fenêtre['fond'] = 'purple'
    fenêtre['épaisseur'] = 5
    position = (25, 15)
    carre(30, fenêtre, position)
```

**vendredi 4/10/22**

**Julien :**

correction de toute les petites erreurs et mise en commun pour les programmes rue.py et forme.py
```Python
# Importation
 
from formes import triangle_equilateral
from formes import rectangle
from random import randint
from formes import triangle_iso
from formes import arc_de_cercle
from formes import carre

#constante
COULEURS_FACADE =['red','blue', 'yellow', 'orange', 'purple', 'green', 'pink', 'black', 'grey', 'brown']
COULEURS_TOIT = ['black']
COULEURS_PORTE = ['black']
COULEURS_FENETRE = ['blue']
# Fonction gestion des données
def couleur(c:list) ->str:
    '''choisit une couleur au hasard parmit celles disponibles
    
    ::param:: c: list contenant les differentes couleurs

    '''
    i = randint(0,len(c) - 1)
    return c[i]


def determiner_immeuble(numero:int) -> dict:
    ''' stock tout les données nécessaire pour créer un immeuble

    ::param:: numero: le numero de l'immeuble (identification)

    '''
    caracteristiques = {}
    caracteristiques['couleur_facade'] = couleur(COULEURS_FACADE)
    caracteristiques['couleur_porte'] = couleur(COULEURS_PORTE)
    caracteristiques['couleur_toit'] = couleur(COULEURS_TOIT)
    caracteristiques['couleur_fenetre'] = couleur(COULEURS_FACADE)
    caracteristiques['numero'] = numero
    caracteristiques['position_m_en_x'] = -300 + numero*(140+70)
    caracteristiques['position_m_en_y'] = -200
    caracteristiques['position_p'] = randint(0,2)
    caracteristiques['etage'] = randint(2, 6)
    caracteristiques['type_toit'] = randint(1, 2)
    return caracteristiques
 
# Fonctions d'interface graphique
 
def dessiner_facade(informations:dict):
    '''créer la façade d'un immeuble
    
    ::param:: informations: contient toutes les information nécessaires à la création d'un immeuble
    
    '''
    facade = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    facade['écriture'] = 'blue'
    facade['fond'] = informations['couleur_facade']
    facade['épaisseur'] = 5
    etage = informations['etage']
    rectangle(140, etage*80, facade, (informations['position_m_en_x'],  informations['position_m_en_y']))
 
def dessiner_porte(informations:dict):
    '''créer la porte d'un immeuble

    ::param:: informations: contient toutes les information nécessaires à la création d'un immeuble

    '''
    porte = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    porte['écriture'] = 'blue'
    porte['fond'] = informations['couleur_porte']
    porte['épaisseur'] = 5
    rectangle(20, 30, porte, (informations['position_m_en_x'] + 20 + 40*informations['position_p'], informations['position_m_en_y']))
    
    
def dessiner_fenetre(informations:dict) -> None:
    '''Dessine un fenêtre
    :::param(informations)::: un dictionnaire contenant les caractéristiques de la fenêtre
    '''
    
    fenetre = {}
    fenetre['écriture'] = 'black'
    fenetre['fond'] = informations['couleur_fenetre']
    fenetre['épaisseur'] = 5
    etage = informations['etage']
    porte = informations['position_p']
    y = informations['position_m_en_y'] + 25
    for e in range(etage):
        if e == 0:
            if porte == 0:
                for i in range (1, 3):
                    x = informations['position_m_en_x'] + 20 * (i*2) + 15
                    carre(30, fenetre, (x, y))
            elif porte == 1:
                for i in range (0, 3, 2):
                    x = informations['position_m_en_x'] + 20 * (i*2) + 15
                    carre(30, fenetre, (x, y))
            else:
                for i in range (2):
                    x = informations['position_m_en_x'] + 20 * (i*2) + 15
                    carre(30, fenetre, (x, y))
        else:
            y = y+80
            for i in range (3):
                x = informations['position_m_en_x'] + 20 * (i*2) + 15
                carre(30, fenetre, (x, y))

def dessiner_toit(informations:dict):
    '''creer le toit d'un batiment

    ::param:: informations: contient toutes les information nécessaires à la création d'un immeuble
    
    '''
    toit= {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    toit['écriture'] = 'blue'
    toit['fond'] = informations['couleur_porte']
    toit['épaisseur'] = 5
    type_toit = informations['type_toit']
    etage = informations['etage']
    if type_toit == 1:
        triangle_iso(toit, (informations['position_m_en_x'], informations['position_m_en_y']+etage*80))
    else:
        arc_de_cercle(70, 180, toit, (informations['position_m_en_x'] + 140, informations['position_m_en_y']+etage*80))

def dessiner_route():
    pass
    
def dessiner_immeuble(informations:dict):
    '''dessine un immeuble à l'aide des fonctions facade, porte et toit

    ::param:: informations: contient toutes les information nécessaires à la création d'un immeuble
    
    '''
    dessiner_facade(informations)
    dessiner_porte(informations)
    dessiner_toit(informations)
    dessiner_fenetre(informations)
    # à compléter avec d'autres fonctions pour le reste : toit, fenêtres...
 
# Programme principal
 


if __name__ == '__main__':

    for x in range(4):
        infos_immeuble = determiner_immeuble(x)
        dessiner_immeuble(infos_immeuble)

```

```Python
'''Ce fichier permet de dessiner deux formes à l'aide des deux fonctions suivantes
 
+ triangle_equilateral(cote, infos, coordonnees)
+ arc_de_cercle(rayon, angle, infos, coordonnees)
 
Exemples d'utilisation :
>>> infos_generales = {'écriture':'blue', 'fond':'#FF88FF', 'épaisseur':5}
>>> triangle_equilateral(50, infos_generales, (50,100))
>>> arc_de_cercle(75, 360, infos_generales, (200,-200))
 
'''
 
# Importation
 
import turtle as trt
import random as rd
 
# Pas de classes
 
# Déclaration des fonctions privées
 
def nouveau_stylo(ecriture, fond, largeur):
    '''Renvoie la référence d'un stylo configuré
 
    :: param ecriture(str)  :: la couleur d'écriture ('red', '#FF0000')
    :: param fond(str)      :: la couleur de fond pour ce stylo
    :: param largeur(int)   :: la largeur du trait
    :: return (Turtle)      :: renvoie un objet de la classe Turtle
 
    '''
    feutre = trt.Turtle()
    feutre.color(ecriture)
    feutre.fillcolor(fond)
    feutre.pensize(largeur)
    feutre.speed(5)
    return feutre
 
def deplacer(feutre, x, y):
    '''Lève le feutre, déplace le feutre et abaisse le feutre
 
    :: param feutre(Turtle) :: la référence de l'objet Turtle
    :: param x(int)         :: coordonnée horizontale (abscisse)
    :: param y(int)         :: coordonnée verticale (ordonnée)
    :: return (None)        :: c'est une fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.penup()# On lève la pointe
    feutre.goto(x, y)  # On déplace le crayon
    feutre.pendown()     # On abaisse la pointe
 
def trace_triangle_equilateral(feutre, cote):
    '''Trace un triangle (equilatéral) à l'aide du crayon feutre
 
    :: param ftr(Turtle)    :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur en pixel des côtés 
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.begin_fill()
    for x in range(3):
        feutre.forward(cote)
        feutre.left(120)
    feutre.end_fill()
    feutre.hideturtle()
 
def trace_triangle_iso(feutre, x,y):
    '''Trace un triangle (isocele) à l'aide du crayon feutre
    :: param feutre(Turtle)    :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur en pixel des côtés 
    :: return (None)        :: fonction sans retour
    :: effet de bord        :: modifie l'état de feutre
    '''
    feutre.begin_fill()
    feutre.goto(x+140,y)
    feutre.left(150)
    feutre.forward(80)
    feutre.left(60)
    feutre.forward(80)
    feutre.left(150)
    feutre.end_fill()
    feutre.hideturtle()
    
def trace_arc(feutre, rayon, angle):
    '''Trace un arc de cercle à l'aide du crayon feutre
 
    :: param ftr(Turtle)    :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur en pixel des côtés 
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.begin_fill()
    feutre.circle(rayon, angle)
    feutre.end_fill()
    feutre.hideturtle()
    
def trace_rectangle(feutre, larg, long):
    '''Trace rectangle à l'aide du crayon feutre
 
    :: param feutre(Turtle)    :: la référence de l'objet Turtle
    :: param rayon(int)     :: la valeur en pixel du rayon
    :: param angle(int)     :: l'angle à tracer (360 pour un cercle)
    :: return (None)        :: fonction sans retour
    .. effet de bord        :: modifie l'état de feutre
 
    '''
    feutre.begin_fill()
    for x in range(4):
        if x == 0 or x == 2 :
            feutre.forward(larg)
            feutre.left(90)
        if x == 1 or x == 3 :
            feutre.forward(long)
            feutre.left(90)
    feutre.end_fill()
def trace_carre(feutre, cote):
    '''Trace un carré à l'aide du crayon feutre
    :: param ftr(Turtle)    :: la référence de l'objet Turtle
    :: param cote(int)      :: la valeur 
    :: return (None)        :: fonction sans retour
 
    '''
    feutre.begin_fill()
    for i in range(4):
        feutre.forward(cote)
        feutre.left(90)
    feutre.end_fill()
    feutre.hideturtle()
    
# Déclarations des fonctions d'interface (aucun paramètre n'est lié au module Turtle)
 
def triangle_equilateral(cote, infos, coordonnees):
    '''Trace un triangle (equilatéral) à partir des infos et aux bonnees coordonnées
 
    :: param cote(int)                     :: la valeur en pixel des côtés
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_triangle_equilateral(feutre, cote)
 
    return feutre
 
def arc_de_cercle(rayon, angle, infos, coordonnees):
    '''Trace un arc de cercle à partir des infos et aux bonnees coordonnées
 
    :: param rayon(int)                    :: la valeur en pixel du rayon
    :: param angle(int)                    :: la valeur en ° de l'angle
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    feutre.left(90)
    trace_arc(feutre, rayon, angle)
 
    return feutre
    
def triangle_iso(infos, coordonnees):
    '''Trace un triangle (isocele) à partir des infos et au bonnes coordonnées
    :: param cote(int)                     :: la valeur en pixel des côtés
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)r
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_triangle_iso(feutre, x, y)
def rectangle(larg, long, infos, coordonnees):
    '''Trace un rectangle à partir des infos et aux bonnees coordonnées
 
    :: param rayon(int)                    :: la valeur en pixel du rayon
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_rectangle(feutre, larg, long)
def carre(cote, infos, coordonnees):
    '''Trace un carré à partir des infos et aux bonnees coordonnées
 
    :: param cote(int)                     :: la valeur en pixel des côtés
    :: param infos(dict)                   :: un dictionnaire {"écriture":str, "fond":str, "épaisseur":int}    
    :: param coordonnees(tuple (int,int) ) :: un tuple (x,y)
 
    '''
    ecriture = infos['écriture']
    fond = infos['fond']
    epaisseur = infos['épaisseur']
    x = coordonnees[0]                  # ou x,y = coordonnees
    y = coordonnees[1]
 
    feutre = nouveau_stylo(ecriture, fond, epaisseur)
    deplacer(feutre, x, y)
    trace_carre(feutre, cote)
 
    return feutre
    
 
# Corps du programme principal
 
if __name__ == '__main__':
 
    infos_generales = {'écriture':'blue', 'fond':'#FF88FF', 'épaisseur':5}
    triangle_equilateral(50, infos_generales, (50,100))
    arc_de_cercle(75, 360, infos_generales, (200,-200))

```
**Lohan et Tanguy**
ajout de deux nouvelles constantes et début de dessiner_route
```Python
COULEURS_ROUTE = 'black'
COULEURS_MARQUAGE = 'white'

def dessiner_route(informations:dict):
    '''on dessine une route'''
    
    route = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    route['écriture'] = 'black'
    route['fond'] = COULEURS_ROUTE
    route['épaisseur'] = 5

    pass
```

**vendredi 14/10/22**

**Julien :**
dans rue.py:
```python
def determiner_immeuble_par_txt(numero:int, infos:list) -> dict:
    ''' stock tout les données nécessaire pour créer un immeuble

    ::param:: numero: le numero de l'immeuble (identification)

    '''
    caracteristiques = {}
    caracteristiques['couleur_facade'] = infos[1]
    caracteristiques['numero'] = numero
    caracteristiques['position_m_en_x'] = -300 + numero*(140+70)
    caracteristiques['position_m_en_y'] = -200
    caracteristiques['position_p'] = infos[3]
    caracteristiques['etage'] = infos[2]
    caracteristiques['type_toit'] = infos[4]
    return caracteristiques
```

**vendredi 21/10/22**

**Julien :**
 dans rue.py
```python
def dessinner_texte(info_immeubles):
    for x in range(len(info_immeuble)):
        infos_immeuble = determiner_immeuble_par_txt(x, info_immeuble[x])
        dessiner_immeuble(infos_immeuble)    
```
** Tanguy et Lohan :**
''' python
def dessiner_route(informations:dict):
    '''on dessine une route'''
    
    route = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    route['écriture'] = 'black'
    route['fond'] = COULEURS_ROUTE
    route['épaisseur'] = 5
    marquage = {}
    marquage['écriture']  = 'white'
    marquage['fond'] = COULEURS_MARQUAGE
    marquage['épaisseur'] = 5
    x = informations['position_m_en_x'] - 200
    y = informations['position_m_en_y'] - 200
    rectangle(910, 100, route, (x,y))
'''