# Model/Cellule.py
#

from Model.Constantes import *

#
# Modélisation d'une cellule de la grille d'un démineur
#


def type_cellule(cell: dict) -> bool:
    """
    Détermine si le paramètre est une cellule correcte ou non

    :param cell: objet dont on veut tester le type cellule
    :return: True si c'est une cellule, False sinon
    """
    return type(cell) == dict and const.CONTENU in cell and const.VISIBLE in cell \
        and type(cell[const.VISIBLE] == bool) and type(cell[const.CONTENU]) == int \
        and (0 <= cell[const.CONTENU] <= 8 or cell[const.CONTENU] == const.ID_MINE)


def isContenuCorrect(en: int) -> bool:
    if type(en) != int :
        retour = False
    elif en >= -1 and en <= 8 :
        retour = True
    else :
        retour = False
    return retour

#def construireCellule(cont = 0, visi = False) -> dict:
    #if isContenuCorrect(cont) == False:
        #raise ValueError(f" construireCellule : le contenu"
                         #f" {cont} n’est pas correct")
    #if type(visi) != bool:
        #raise TypeError(f"construireCellule : le second "
                        #f"paramètre {type(visi)} "
                        #f"n’est pas un booléen")
    #if cont == -1:
        #dico = {'const.ID_MINE' : cont, 'const.VISIBLE' : visi}
    #else :
        #dico = {'const.CONTENU' : cont, 'const.VISIBLE' : visi}
    #print(type(dico))
    #return dico

