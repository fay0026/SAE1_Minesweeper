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
    lisTemp = []
    grille = []
    for i in range(nl):
        for j in range(nc):
            lisTemp.append(construireCellule())
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

def getCelluleGrilleDemineur(grille: list, coord: tuple) -> dict :
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

def getCoordonneeVoisinsGrilleDemineur(grille: list, coord: tuple) -> list:
    if type(coord) != tuple or len(coord) > 2 or type_grille_demineur(grille) == False :
        raise TypeError(f"getCoordonneeVoisinsDemineur : un des paramètres n’est pas du bon type.")
    if isCoordonneeCorrecte(grille, coord) == False :
        raise IndexError(f"getCoordonneeVoisinsGrilleDemineur : la coordonnée n’est pas dans la grille")
    coordVoisins = []
    #Test de chaque case à partir de [0]+1, jusqu'à [0]-1 [1]+1
    if isCoordonneeCorrecte(grille, (coord[0]+1, coord[1])) :
        coordVoisins.append((coord[0]+1, coord[1]))
    if isCoordonneeCorrecte(grille, (coord[0], coord[1]+1)) :
        coordVoisins.append((coord[0], coord[1]+1))
    if isCoordonneeCorrecte(grille, (coord[0]+1, coord[1]+1)):
        coordVoisins.append((coord[0]+1, coord[1]+1))
    if isCoordonneeCorrecte(grille, (coord[0]-1, coord[1])):
        coordVoisins.append((coord[0]-1, coord[1]))
    if isCoordonneeCorrecte(grille, (coord[0], coord[1]-1)) :
        coordVoisins.append((coord[0], coord[1]-1))
    if isCoordonneeCorrecte(grille, (coord[0]-1, coord[1]-1)) :
        coordVoisins.append((coord[0]-1, coord[1]-1))
    if isCoordonneeCorrecte(grille, (coord[0]+1, coord[1]-1)) :
        coordVoisins.append((coord[0]+1, coord[1]-1))
    if isCoordonneeCorrecte(grille, (coord[0]-1, coord[1]+1)) :
        coordVoisins.append((coord[0]-1, coord[1]+1))
    return coordVoisins

def placerMinesGrilleDemineur(grille: list, nb: int, coord: tuple) -> None:
    if nb <= 0 or nb >= (getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille)) :
        raise ValueError(f"« placerMinesGrilleDemineur : Nombre de bombes à placer incorrect ")
    if isCoordonneeCorrecte(grille, coord) == False:
        raise IndexError(f"placerMinesGrilleDemineur : la coordonnée n’est pas dans la grille.")
    ranCoord = ((randint(0, getNbLignesGrilleDemineur(grille) - 1)),
                ((randint(0, getNbColonnesGrilleDemineur(grille) - 1))))
    for i in range(nb):
        while ranCoord == coord or contientMineGrilleDemineur(grille, ranCoord) == True:
            ranCoord = ((randint(0, getNbLignesGrilleDemineur(grille)-1)),
                        ((randint(0, getNbColonnesGrilleDemineur(grille)-1))))
        cellTemp = getCelluleGrilleDemineur(grille, ranCoord)
        setContenuCellule(cellTemp, -1)
    compterMinesVoisinesGrilleDemineur(grille)
    return None

def compterMinesVoisinesGrilleDemineur(grille: list) -> None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if contientMineGrilleDemineur(grille, (i,j)) == False :
                voisinsTemp = getCoordonneeVoisinsGrilleDemineur(grille, (i,j))
                compteur = 0
                for k in range(len(voisinsTemp)):
                    if contientMineCellule(getCelluleGrilleDemineur(grille, voisinsTemp[k])) == True :
                        compteur += 1
                setContenuGrilleDemineur(grille, (i,j), compteur)
    return None

def getNbMinesGrilleDemineur(grille: list) -> int:
    if type_grille_demineur(grille) == False :
        raise ValueError(f"getNbMinesGrilleDemineur : Le paramètre n’est pas une grille")
    compteur = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if contientMineGrilleDemineur(grille, (i,j)) == True :
                compteur += 1
    return compteur

def getAnnotationGrilleDemineur(grille: list, coord: tuple) -> str:
    return getAnnotationCellule(getCelluleGrilleDemineur(grille, coord))

def getMinesRestantesGrilleDemineur(grille: list) -> int:
    compteur = 0
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if getCelluleGrilleDemineur(grille, (i,j))[const.ANNOTATION] == const.FLAG:
                compteur += 1
    return getNbMinesGrilleDemineur(grille) - compteur

def gagneGrilleDemineur(grille: list) -> bool:
    CasesNope = getNbLignesGrilleDemineur(grille) * getNbColonnesGrilleDemineur(grille)
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if contientMineGrilleDemineur(grille, (i,j)) == True and getCelluleGrilleDemineur(grille, (i,j))[const.ANNOTATION] \
                    == const.FLAG and getCelluleGrilleDemineur(grille, (i,j))[const.VISIBLE] == False :
                CasesNope -= 1
            elif getCelluleGrilleDemineur(grille, (i,j))[const.VISIBLE] == True and contientMineGrilleDemineur(grille, (i,j)) == False :
                CasesNope -= 1
    if CasesNope == 0:
        gagne = True
    else :
        gagne = False
    return gagne

def perduGrilleDemineur(grille: list) -> bool :
    perdu = False
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            if contientMineGrilleDemineur(grille, (i, j)) == True and getCelluleGrilleDemineur(grille, (i,j))[const.VISIBLE] == True :
                perdu = True
    return perdu

def reinitialiserGrilleDemineur(grille: list) -> None:
    for i in range(getNbLignesGrilleDemineur(grille)):
        for j in range(getNbColonnesGrilleDemineur(grille)):
            reinitialiserCellule(getCelluleGrilleDemineur(grille, (i, j)))
    return None

def decouvrirGrilleDemineur(grille: list, coord: tuple, aDecouvrir = set()) -> set:
    aDecouvrir.add(coord)
    if getCelluleGrilleDemineur(grille, coord)[const.CONTENU] == 0:
        voisins = getCoordonneeVoisinsGrilleDemineur(grille, coord)
        for i in range(len(voisins)):
            if getCelluleGrilleDemineur(grille, voisins[i])[const.CONTENU] == 0 and voisins[i] not in aDecouvrir:
                aDecouvrir.add(voisins[i])
                decouvrirGrilleDemineur(grille, voisins[i], aDecouvrir)
    return aDecouvrir