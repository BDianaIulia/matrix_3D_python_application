###modul pentru generarea valorilor random - Testarea functiilor lucrului cu
###matrici rare tridimensionale
import random

#random.randrange( stop ) returneaza un numar random ce apartine intervalului [0, stop)


#generator de matrice random
def randomMatrix():
    MyList = []
    n = random.randrange(71)        #generam numarul de elemente
    for iterator in range(n):       #generam n elemente, fiecare element avand 3 indici si o valoare
        i = random.randrange(6)
        j = random.randrange(6)
        k = random.randrange(6)
        value = random.randrange(999) + 1           #adaugand 1, ne asiguram ca are valoare nenula
        MyList.append( (i , j , k , value) )        #adaugam intr-o lista sub forma de tuplu

    MyList.sort()                   #sortam lista 
    return MyList                   #returnam o lista de tupluri


#generator de indici random ( pentru a putea cauta valoarea de la indicii respectivi )
def randomValueToRead():
    first = random.randrange(6)
    second = random.randrange(6)
    third = random.randrange(6)
    return (first, second, third)   #returneaza un tuplu format din trei indici


#generator de element random ( pentru a putea adauga valoarea la indicii respectivi )
def randomValueToWrite():
    first = random.randrange(6)
    second = random.randrange(6)
    third = random.randrange(6)
    newValue = random.randrange(999) + 1            #adaugand 1, ne asiguram ca are valoare nenula
    return( first , second , third , newValue )     #returneaza un tuplu care alcatuieste elementul


#generator de dimensiune random pentru matrice unitate
def randomValueForUnitMatrix():
    length = random.randrange(6)    #fiind matrice patratica, este necesara doar o valoare a dimensiunii
    if length == 0:                 #daca valoarea generata este 0, reapelam functia pentru a cauta o alta valoare
        length = randomValueForUnitMatrix()
    return length                   #returnam o valoare


#generator de dimensiuni pentru o matrice nula
def randomIndexesForNullMatrix():
    maxI = random.randrange(6)
    maxJ = random.randrange(6)
    maxK = random.randrange(6)
    return (maxI , maxJ, maxK)      #returnam un tuplu format din cele trei dimensiuni

