# GrilleDemineur.py

from Model.Cellule import *
from Model.Coordonnee import *
from random import shuffle, randint
from itertools import filterfalse


# Méthode gérant la grille du démineur
# La grille d'un démineur est un tableau 2D régulier (rectangulaire)
#
# Il s'agira d'une liste de liste


def type_grille_demineur(grille: list) -> bool:
    """
    Détermine si le paramètre représente une grille d'un démineur.

    :param grille: objet à tester
    :return: `True` s'il peut s'agit d'une grille de démineur, `False` sinon
    """
    if type(grille) != list:
        return False
    # Récupération du nombre de lignes
    nl = len(grille)
    # Il faut que la grille comporte au moins une ligne
    if nl == 0:
        return False
    nc = len(grille[0])
    if nc == 0:
        return False
    return next(filterfalse(lambda line: type(line) == list and len(line) == nc
                            and next(filterfalse(type_cellule, line), True) is True, grille), True) is True
    # Tableau régulier
    # nc = None
    # for line in grille:
    #     if type(line) != list:
    #         return False
    #     if nc is None:
    #         nc = len(line)
    #         # Il faut que la grille comporte au moins une colonne
    #         if nc == 0:
    #             return False
    #     elif nc != len(line):
    #         return False
    #     # Test des cellules de la ligne
    #     if not next(filterfalse(type_cellule, line), True):
    #         return False
    # for cell in line:
    #     if not type_cellule(cell):
    #         return False
    # return True

def construireGrilleDemineur(nl: int, nc: int):
    if nl <= 0 or nc <= 0 :
        raise ValueError(f"construireGrilleDemineur : Le "
                         f"nombre de lignes {nl} "
                         f"ou de colonnes {nc} est négatif ou nul. ")
    if type(nl) != int or type(nc) != int :
        raise TypeError(f"construireGrilleDemineur : Le nombre de lignes "
                        f"{nl} ou de colonnes {nl} n’est pas un entier. ")
    cellTemp = construireCellule()
    lisTemp = []
    grille = []
    for i in range(nl):
        for j in range(nc):
            lisTemp.append(cellTemp)
        grille.append(lisTemp)
        lisTemp = []
    return grille

def getNbLignesGrilleDemineur(grille: list) -> int :
    if type_grille_demineur(grille) != True :
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille)

def getNbColonnesGrilleDemineur(grille: list) -> int :
    if type_grille_demineur(grille) != True :
        raise TypeError(f"getNbLignesGrilleDemineur : Le paramètre n’est pas une grille")
    return len(grille[0])

def isCoordonneeCorrecte(grille: list, coord: tuple) -> bool :
    if type(coord) != tuple or len(coord) > 2 or type_grille_demineur(grille) == False :
        raise TypeError(f"isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    check = False
    if coord[0] >= 0 and coord[0] < getNbLignesGrilleDemineur(grille) and \
            coord[1] >= 0 and coord[1] < getNbColonnesGrilleDemineur(grille):
        check = True
    return check

def getCelluleGrilleDemineur(grille: list, coord: tuple) -> int :
    if type(coord) != tuple or len(coord) > 2 or type_grille_demineur(grille) == False :
        raise TypeError(f"isCoordonneeCorrecte : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord) == False :
        raise IndexError(f"getCelluleGrilleDemineur : coordonnée non "
                         f"contenue dans la grille.")
    return grille[coord[0]][coord[1]]

def getContenuGrilleDemineur(grille: list, coord: tuple) -> int:
    return getContenuCellule(getCelluleGrilleDemineur(grille, coord))

def setContenuGrilleDemineur(grille: list, coord: tuple, cont: int) -> None:
    return setContenuCellule(getCelluleGrilleDemineur(grille, coord), cont)

def isVisibleGrilleDemineur(grille: list, coord: tuple) -> bool:
    return isVisibleCellule(getCelluleGrilleDemineur(grille, coord))

def setVisibleGrilleDemineur(grille: list, coord: tuple, visi: bool) -> None:
    setVisibleCellule(getCelluleGrilleDemineur(grille, coord), visi)
    return None

def contientMineGrilleDemineur(grille: list, coord: tuple) -> bool:
    return contientMineCellule(getCelluleGrilleDemineur(grille, coord))

