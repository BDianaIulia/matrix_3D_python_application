###modul de functii - Functii necesare lucrului cu matrici rare tridimensionale

#citim valorile matricii tridimensionale de la tastatura cu scopul de a creea o lista
def readValues(): 
    newMatrix = []          #initiem o lista goala
    print('Enter the number of terms:')
    n = input("n=")         #citim numarul elementelor nenule dorite a fi introduse
    print('Enter the terms and their index:')

                            #citim cei trei indici si valoarea de la indicii respectivi intr-o singura linie
                            #si ii adaugam in lista noastra sub forma de tuplu
    while n > 0:            
        first, second, third, value = raw_input().split()   
        tupl = (int(first) , int(second) , int(third) , int(value) )
        newMatrix.append(tupl)
        n -= 1
        
                            #folosim functia predefinita pentru a sorta lista de tupluri
    newMatrix.sort()    
    return newMatrix        #functia returneaza lista creata
    




#cautam dimensiunile matricii tridimensionale
def maxIndex( Matrix ):             #functia are ca parametru o lista de tupluri
    maxi = 0                            
    maxj = 0                        #dimensiunea matricii este data de cei mai mari indici din lista
    maxk = 0
    for obiect in Matrix:           #Iteram in lista. Variabila obiect se asigneaza ca tuplu
        if obiect[0] > maxi:        #obiect[0] reprezinta primul indice al elementului din matrice
            maxi = obiect[0] 
        if obiect[1] > maxj:        #obiect[1] reprezinta cel de-al doilea indice al elementului din matrice
            maxj = obiect[1] 
        if obiect[2] > maxk:        #obiect[2] reprezinta cel de-al treilea indice al elementului din matrice
            maxk = obiect[2] 
            
    return (maxi , maxj , maxk)     #functia returneaza un tuplu format din cele 3 dimensiuni





#cautam un element al matricii tridimensionale dupa indici
def readAValue( first, second, third , Matrix ):    #functia are ca parametrii indicii pentru valoarea cautata
                                                    #si o lista de tupluri
    
    max_index = maxIndex( Matrix )                  #functie definita anterior
    maxi = max_index[0]
    maxj = max_index[1]                             #dimensiunile maxime ale matricii
    maxk = max_index[2]
    if first > maxi or second > maxj or third > maxk :      #daca se primesc indici ce nu apartin matricii
        #print("Limited exceeded")
        return None                                         #returnam None
    
    for obiect in Matrix:                           #iteram prin Lista. Variabilei 'obiect' i se asigneaza un tuplu
        if first == obiect[0]:
            if second == obiect[1]:
                if third == obiect[2]:              #daca s-a gasit un element aflat pe pozitia indicilor specificati
                    return obiect[3]                #returnam valoarea elementului
    return 0                                        #altfel, elementul are valoarea 0, pe care o returnam





#scriem o valoare la indicii specificati
def writeAValue( first, second, third, newValue, Matrix ):  #parametrii sunt cei trei indici, valoarea elementului
                                                            #si lista de tuplu si formeaza matricea
    max_index = maxIndex( Matrix )                  #functie definita anterior
    maxi = max_index[0]
    maxj = max_index[1]                             #dimensiunile matricii
    maxk = max_index[2]
    if first > maxi or second > maxj or third > maxk :      #daca se primesc indici ce depasesc dimensiunile matricii
        #print("Limited exceeded")
        return False                                #returnam False


    #se trateaza 2 cazuri:
    #-daca exista deja un element la pozitia specificata, trebuie modificat( pentru ca tuplul este un container imutabil,
                                    #elementul vechi trebuie scos, pentru ca apoi sa-l readaugam cu valoarea noua )
    #-daca nu exista, trebuie inserat la pozitia corespunzatoare, tinand cont ca lista e sortata
    
    #daca am inserat elementul, returnam True
    
    
    it = 0                                          #initializam iteratorul cu 0. Aceasta variabila contorizeaza cate cicluri
                                                                #s-au realizat in for
    for obiect in Matrix:                           #iteram prin lista. Variabilei obiect i se asigneaza un tuplu
        if first == obiect[0]:              
            if second == obiect[1]:
                if third == obiect[2]:              #daca s-a gasit un element aflat pe pozitia celor trei indici 
                    Matrix.pop(it)                  #eliminam elementul (care se afla pe pozitia it)
                    Matrix.insert(it , (first, second, third, newValue))    #il readaugam, pe aceeasi pozitie, dupa abdatare
                    return True
                #avand in vedere ca lista este sortata, cum am gasit primul element care are indicii mai mari, ne oprim pentru
                #a insera pe acea pozitie 
                elif third < obiect[2]:             
                    Matrix.insert(it , (first, second, third, newValue))
                    return True
            elif second < obiect[1]:
                Matrix.insert(it , (first, second, third, newValue))
                return True
        elif first < obiect[0]:
            Matrix.insert(it , (first, second, third, newValue))
            return True
        it = it + 1                                 

    #daca s-a terminat bucla, fara a se insera elementul, inseamna ca acesta trebuie inserat pe ultima pozitie
    Matrix.insert(it , (first, second, third, newValue))    
    return True                                     

    


#afisam matricea tridimensionala corespondenta listei de tupluri
def displayMatrix( Matrix , fileName ):     #paramerii sunt reprezentati de o lista de tupluri si un obiect fisier
    max_index = maxIndex( Matrix )          #functie definita anterior
    maxi = max_index[0]
    maxj = max_index[1]
    maxk = max_index[2]                     #dimeniunile matricii


    #cu ajutorul a trei for-uri, iteram prin intreaga matrice
    #cu ajutorul functiei 'readAValue()' definita anterior, verificam ce valoare se afla pe fiecare pozitie
    for first_index in range(0 , maxi + 1):
        for second_index in range(0 , maxj + 1):
            for third_index in range(0 , maxk + 1):
                fileName.write(str(readAValue( first_index, second_index,
                                  third_index, Matrix )) + ' '),        
            fileName.write('\n')
        fileName.write('\n\n')





#crearea unei matrici unitate (toate elementele de pe diagonala principala au valoarea 1, restul avand valoarea 0 )
#matricea unitate este patratica( cele 3 dimensiuni sunt egale )
def unitMatrix( length ):               #parametrul reprezinta dimensiunea matricei
    unit_matrix = []
    for iterator in range(0 , length + 1):      #trebuie adaugate exact 'length' valori
                                                #la pozitile 1,1,1 ; 2,2,2 ; .. ; n,n,n;
        unit_matrix.append( (iterator , iterator, iterator , 1) )   

    return unit_matrix;                 #functia returneaza o lista de tupluri





#crearea uni matrici nule tridimensionale (toate elementele au valoare nula)
#pentru a putea sa o cream, trebuie sa memoram ultimul element, desi acesta are valoarea 0, pentru a putea
#stii dimensiunea matricii

def nullMatrix( maxI, maxJ, maxK ):     #parametrii reprezinta cele trei dimensiuni ale matricii
    null_matrix = [(maxI, maxJ, maxK, 0)]
    return null_matrix                  #returnam o lista de tupluri





#adunarea a doua matrici tridimensionale
#in mod normal, adunarea se realizeaza doar daca cele doua matrici au dimensiuni egale
#Pentru a mari aria de acoperire a problemei, vom considera extinderea matricii cu dimensiuni
#mai mici pana la dimensiunile celei de-a doua prin adaugare de valori de 0.

def addMatrix( Matrix1 , Matrix2 ):         #parametrii reprezinta doua liste de tupluri
    max_index1 = maxIndex( Matrix1 )        #'maxIndex()' este functie definita anterior
    max_index2 = maxIndex( Matrix2 )        #salvam dimensiunile celor doua matrici
    #if max_index1 != max_index2:
        #print( "The matrix need to have same lengths" )
        #return
    max_index = max( max_index1, max_index2 )       #pastram dimensiunea matricii mai mare

    addMatrix = []
    
    #cu ajutorul a trei for-uri, traversam toate combinatiile de indici pe care le putem avea
    for first_index in range(0 , max_index[0] + 1):
        for second_index in range(0 , max_index[1] + 1):
            for third_index in range(0, max_index[2] + 1):
                firstValue = readAValue( first_index, second_index,     #'readAValue()' este o functie definita anterior
                                         third_index, Matrix1 )         #valoarea din prima matrice de la indicii respectivi
                secondValue = readAValue( first_index, second_index,
                                         third_index, Matrix2 )         #valoarea din a doua matrice
                
                #daca valoarea este None( indicii nu fac parte din matricea respectiva ) , convertim valoarea la 0
                if firstValue == None:                  
                    firstValue = 0

                if secondValue == None:
                    secondValue = 0

                #daca suma celor doi termeni dau 0 , aceasta valoare nu trebuie memorata
                if firstValue + secondValue != 0:           
                    addMatrix.append(( first_index, second_index,       
                                     third_index, firstValue + secondValue ))
                #deoarece indicii itereaza crescator, lista va fi implicit sortata( nu este necesar sa o mai sortam )

    return addMatrix                                                    #returnam o lista de tupluri





#scaderea a doua matrici tridimensionale
#in mod normal, scaderea se realizeaza doar daca cele doua matrici au dimensiuni egale
#Pentru a mari aria de acoperire a problemei, vom considera extinderea matricii cu dimensiuni
#mai mici pana la dimensiunile celei de-a doua prin adaugare de valori de 0.

def substituteMatrix( Matrix1 , Matrix2 ):
    max_index1 = maxIndex( Matrix1 )
    max_index2 = maxIndex( Matrix2 )
    #if max_index1 != max_index2:
        #print( "The matrix need to have same lengths" )
        #return
    
    max_index = max( max_index1, max_index2 )                           #pastram dimensiunea matricii mai mare
    
    subList = []

    #cu ajutorul a trei for-uri, traversam toate combinatiile de indici pe care le putem avea
    for first_index in range(0 , max_index[0] + 1):
        for second_index in range(0 , max_index[1] + 1):
            for third_index in range(0 , max_index[2] + 1):
                firstValue = readAValue( first_index, second_index,      #'readAValue()' este o functie definita anterior
                                         third_index, Matrix1 )          #valoarea din prima matrice de la indicii respectivi
                secondValue = readAValue( first_index, second_index,
                                         third_index, Matrix2 )          #valoarea din a doua matrice

                #daca valoarea este None( indicii nu fac parte din matricea respectiva ) , convertim valoarea la 0
                if firstValue == None:
                    firstValue = 0

                if secondValue == None:
                    secondValue = 0

                #daca diferenta celor doi termeni dau 0 , aceasta valoare nu trebuie memorata
                if firstValue - secondValue != 0:
                    subList.append(( first_index, second_index,
                                     third_index, firstValue - secondValue ))

                #deoarece indicii itereaza crescator, lista va fi implicit sortata( nu este necesar sa o mai sortam )

    return subList                                                      #returnam o lista de tupluri
