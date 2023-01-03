# Coordonnee.py

import const

# Définition des coordonnées (ligne, colonne)


def type_coordonnee(coord: tuple) -> bool:
    """
    Détermine si le paramètre correspond ou non à une coordonnée.

    Cette fonction teste notamment si les lignes et colonnes sont bien positives. Dans le cas contraire, la fonction
    retourne `False`.

    :param coord: couple représentant le numéro de ligne et celui de la colonne (commençant les deux à 0)
    :return: `True` si le paramètre correspond à une coordonnée, `False` sinon.
    """
    return type(coord) == tuple and len(coord) == 2 and type(coord[0]) == int and type(coord[1]) == int \
        and coord[0] >= 0 and coord[1] >= 0


def construireCoordonnee(l: int, c: int) -> tuple:
    if type(l) != int or type(c) != int:
        raise TypeError(f"construireCoordonnee : Le numéro de ligne "
                        f"{type(l)} ou le numéro de colonne "
                        f"{type(c)} ne sont pas des entiers ")
    if l < 0 or c < 0:
        raise ValueError(f"construireCoordonnee : Le numéro de ligne {l}"
                         f"ou de colonne {c} ne sont pas positifs")
    return (l, c)

def getLigneCoordonnee(coor: tuple) -> int:
    if type_coordonnee(coor) == False:
        raise TypeError(f"getLigneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coor[0]

def getColonneCoordonnee(coor: tuple) -> int:
    if type_coordonnee(coor) == False:
        raise TypeError(f"getColonneCoordonnee : Le paramètre n’est pas une coordonnée")
    return coor[1]

