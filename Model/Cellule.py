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

def getContenuCellule(dico: dict) -> int:
    if type_cellule(dico) == False :
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule.")
    return dico['const.CONTENU']

def isVisibleCellule(dico: dict) -> bool:
    if type_cellule(dico) == False :
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule.")
    return dico['const.VISIBLE']

def setContenuCellule(dico: dict, cont: int) -> None:
    if type_cellule(dico) == False :
        raise TypeError(f"getContenuCellule : Le premier paramètre n'est pas une cellule.")
    if cont != int :
        raise TypeError(f"setContenuCellule : Le second paramètre n'est pas un entier")
    if isContenuCorrect(cont) == False:
        raise ValueError(f"setContenuCellule : la valeur du contenu {cont} n'est"
                         f"pas correcte.")
    dico['const.CONTENU'] = cont
    return dico

def setVisibleCellule(dico: dict, visi: bool) -> None:
    if type_cellule(dico) == False :
        raise TypeError(f"getContenuCellule : Le premier paramètre n'est pas une cellule.")
    if visi != bool:
        raise TypeError(f"setContenuCellule : Le second paramètre n'est pas un entier")
    dico['const.VISIBLE'] = visi
    return dico

def contientMineCellule(dico: dict) -> bool:
    if type_cellule(dico) == False :
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule.")
    presence = False
    if dico['const.CONTENU'] == -1:
        presence = True
    return presence

