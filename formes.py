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



