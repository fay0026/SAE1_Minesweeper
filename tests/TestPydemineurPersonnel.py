import unittest
import const

from Model.Cellule import *
from Model.GrilleDemineur import *
from random import randint

#print(getContenuCellule({const.CONTENU : 5, const.VISIBLE : False}))

#print(construireCellule())
#print(construireCellule(5, False))
#print(construireCellule(0, True))
#print(construireCellule(-1, True))
#print(construireCellule())

#print(isCoordonneeCorrecte(construireGrilleDemineur(2,3), (0,0)))
#print(isCoordonneeCorrecte(construireGrilleDemineur(2,3), (1,1)))
#print(isCoordonneeCorrecte(construireGrilleDemineur(2,3), (2,3)))

#print(getCoordonneeVoisinsGrilleDemineur(construireGrilleDemineur(2,3), ((1,1))))

ranCoord = (())
grille = construireGrilleDemineur(2,3)
randint(0,5)
for i in range(10):
    print(len(grille))
    print(len(grille[0]))
    coordTemp1 = randint(0, len(grille)-1)
    coordTemp2 = randint(0, len(grille[0])-1)
    ranCoord = (coordTemp1, coordTemp2)
    if isCoordonneeCorrecte(grille, ranCoord) == False :
        print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    print(ranCoord)
    print(type(ranCoord))