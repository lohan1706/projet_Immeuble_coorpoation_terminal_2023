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
COULEURS_ROUTE = 'black'
COULEURS_MARQUAGE = 'white'
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

def dessiner_route(informations:dict):
    '''on dessine une route'''
    
    route = {}  # pour faire la "traduction" entre les clés de ce module et les clés du module formes
    route['écriture'] = 'black'
    route['fond'] = COULEURS_ROUTE
    route['épaisseur'] = 5

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

def dessinner_texte(info_immeubles):
    for x in range(len(info_immeuble)):
        infos_immeuble = determiner_immeuble_par_txt(x, info_immeuble[x])
        dessiner_immeuble(infos_immeuble)    
# Programme principal
 


if __name__ == '__main__':

    for x in range(4):
        infos_immeuble = determiner_immeuble(x)
        dessiner_immeuble(infos_immeuble)
