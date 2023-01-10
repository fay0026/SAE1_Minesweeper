import unittest
import const

from Model.Cellule import *
from Model.Constantes import *
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

#ranCoord = (())
#grille = construireGrilleDemineur(2,3)
#randint(0,5)
#for i in range(10):
    #print(len(grille))
    #print(len(grille[0]))
    #coordTemp1 = randint(0, len(grille)-1)
    #coordTemp2 = randint(0, len(grille[0])-1)
    #ranCoord = (coordTemp1, coordTemp2)
    #if isCoordonneeCorrecte(grille, ranCoord) == False :
        #print("AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA")
    #print(ranCoord)
    #print(type(ranCoord))

#for i in range(4):
    #print(i)

#word_freq = {
    #"Hello": 56,
    #"at": 23,
     #const.ANNOTATION : 43,
    #"this": 78
}
#key = const.ANNOTATION

#if key in word_freq:
    #print(f"Yes, key: '{key}' exists in dictionary")
#else:
    #print(f"No, key: '{key}' does not exists in dictionary")

#cell = {const.CONTENU: 0, const.VISIBLE: False}
#print(getAnnotationCellule(cell))
#print("important")
#print(isAnnotationCorrecte("N'importe quoi !"))

