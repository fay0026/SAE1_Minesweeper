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

print(isCoordonneeCorrecte(construireGrilleDemineur(2,3), (0,0)))
print(isCoordonneeCorrecte(construireGrilleDemineur(2,3), (1,1)))
print(isCoordonneeCorrecte(construireGrilleDemineur(2,3), (2,3)))