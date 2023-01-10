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

def construireCellule(cont: int = 0, visible: bool = False) -> dict:
    if isContenuCorrect(cont) == False:
        raise ValueError(f" construireCellule : le contenu"
                         f" {cont} n’est pas correct")
    if type(visible) != bool:
        raise TypeError(f"construireCellule : le second "
                        f"paramètre {type(visible)} "
                        f"n’est pas un booléen")
    dico = {const.CONTENU : cont, const.VISIBLE : visible, const.ANNOTATION : None}
    return dico

def getContenuCellule(cell: dict) -> int:
    if type_cellule(cell) == False :
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule.")
    return cell[const.CONTENU]

def isVisibleCellule(cell: dict) -> bool:
    if type_cellule(cell) == False :
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule.")
    return cell[const.VISIBLE]

def setContenuCellule(cell: dict, cont: int) -> None:
    if type_cellule(cell) == False :
        raise TypeError(f"getContenuCellule : Le premier paramètre n'est pas une cellule.")
    if type(cont) != int :
        raise TypeError(f"setContenuCellule : Le second paramètre n'est pas un entier")
    if isContenuCorrect(cont) == False:
        raise ValueError(f"setContenuCellule : la valeur du contenu {cont} n'est"
                         f"pas correcte.")
    cell[const.CONTENU] = cont
    return cell

def setVisibleCellule(cell: dict, visi: bool) -> None:
    if type_cellule(cell) == False :
        raise TypeError(f"getContenuCellule : Le premier paramètre n'est pas une cellule.")
    if type(visi) != bool:
        raise TypeError(f"setContenuCellule : Le second paramètre n'est pas un entier")
    cell[const.VISIBLE] = visi
    return cell

def contientMineCellule(cell: dict) -> bool:
    if type_cellule(cell) == False :
        raise TypeError(f"getContenuCellule : Le paramètre n'est pas une cellule.")
    presence = False
    if cell[const.CONTENU] == -1:
        presence = True
    return presence

def isAnnotationCorrecte(anno: str) -> bool:
    retour = False
    if anno == const.DOUTE or anno == const.FLAG or anno == None :
        retour = True
    return retour

def getAnnotationCellule(cell: dict) -> str:
    if type_cellule(cell) == False :
        raise TypeError(f"getAnnotationCellule : le paramètre valeur_du "
                        f"paramètre n’est pas une cellule")
    if const.ANNOTATION not in cell:
        retour = None
    else :
        retour = cell[const.ANNOTATION]
    return retour

