import functions as file1
import generator as file2
###modul principal - Lucru cu matrici rare tridimensionale in care se
###stocheaza doar valorile nenule prin indici

###In acest modul verificam functiile prin valori create random.

n = 5
while n:
    File = open('test'+ str(n) , 'w')

    #Cream prima matrice si o afisam
    Matrix1 = file2.randomMatrix()
    File.write('Matrix looks like: \n')
    file1.displayMatrix( Matrix1 , File )
    File.write('\n\n')


    #afisam dimensiunile matricii
    max_indexes = file1.maxIndex( Matrix1 )
    File.write('Dimension of the matrix is: \n' )
    File.write('{} x {} x {} \n'.format( max_indexes[0] + 1,
                                 max_indexes[1] + 1, max_indexes[2] + 1 ))
    File.write( '\n\n' )


    #cautam valoarea unui element referentiat prin indici
    indexes = file2.randomValueToRead()
    value = file1.readAValue( indexes[0], indexes[1], indexes[2], Matrix1 )
    if value == None:
        File.write('Limited exceeded\n')
    else:
        File.write('The value at the indexes {}, {}, {} are: {}\n'.format( indexes[0],
                                    indexes[1], indexes[2], value ) )
    File.write('\n\n')


    #scriem o valoare in matrice a unui element referentiat prin indici
    new_elem = file2.randomValueToWrite()
    value = file1.writeAValue( new_elem[0], new_elem[1], new_elem[2],
                               new_elem[3], Matrix1 )
    if value == False:
        File.write('Limited exceeded\n')
    else:
        File.write('The value at the indexes {}, {}, {} now are: {}\n'.format( new_elem[0],
                                    new_elem[1], new_elem[2], new_elem[3] ) )
    file1.displayMatrix( Matrix1, File )
    File.write('\n\n')




    #constuim o a doua matrice
    File.write('Now, we build a new matrix: \n')
    Matrix2 = file2.randomMatrix()
    File.write('Matrix looks like: \n')
    file1.displayMatrix( Matrix2, File )
    File.write('\n\n')


    #afisam dimensiunile ei
    max_indexes = file1.maxIndex( Matrix2 )
    File.write('Dimension of the matrix is:\n' )
    File.write('{} x {} x {}\n'.format( max_indexes[0] + 1,
                                 max_indexes[1] + 1, max_indexes[2] + 1 ))
    File.write( '\n\n' )



    #adunam cele doua matrici construite anterior
    File.write('After addition, the result matrix looks like: \n')
    add_matrix = file1.addMatrix( Matrix1, Matrix2 )
    file1.displayMatrix( add_matrix, File )
    File.write('\n\n')


    #scadem cele doua matrici construite anterior
    File.write('After substitution, the result matrix looks like: \n')
    sub_matrix = file1.substituteMatrix( Matrix1, Matrix2 )
    file1.displayMatrix( sub_matrix, File )
    File.write('\n\n')



    #constuim o matrice unitate si o afisam
    length = file2.randomValueForUnitMatrix()
    File.write('Unit Matrix with the length {} looks like: \n'.format( length + 1 ) )
    unit_matrix = file1.unitMatrix( length )
    file1.displayMatrix( unit_matrix, File )


    #construim o matrice nula
    dimension = file2.randomIndexesForNullMatrix()
    null_matrix = file1.nullMatrix( dimension[0], dimension[1], dimension[2] )
    File.write('Has been created a null matrix with dimension: \n')
    File.write('{} x {} x {}\n'.format( dimension[0] + 1, dimension[1] + 1, dimension[2] + 1))
    #afisam lista creata pentru aceasta matrice
    File.write( str(null_matrix) + '\n')

    File.close()
    n -= 1
