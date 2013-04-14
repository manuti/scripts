import numpy as np
import math as m

dim = 4
coordenada = m.sqrt(dim)
#definicion de la matriz
x = np.zeros((dim,dim))
x[0] = [2,0,0,0]
x[1] = [0,0,1,0]
x[2] = [0,2,0,0]
x[3] = [0,0,0,4]

#defino los arrays
i = 0
fila = [0] * dim
columna = [0] * dim
submatriz = [0] * dim

#metemos las filas en una array
while i < dim :
 fila[i] = x[i]
 print 'Fila ' + str(i)
 print (fila[i])
 i = i + 1

#metemos las columnas en una array
i = 0
while i < dim :
 columna[i] = x[:,i]
 print 'Columna ' + str(i)
 print (columna[i])
 i = i + 1

#metemos las submatrices en una array
i = 0
while i < dim :
 resto = i%coordenada
 division = int (i/coordenada)
 submatriz[i] = x[coordenada*division:coordenada*(division+1),resto*coordenada:coordenada*(resto+1)]
 #print 'coordenada vale ' + str(coordenada) + ', e i vale ' + str(i)
 #print 'Resto ' + str(resto)
 #print 'Division ' + str(division)
 print 'Submatriz ' + str(i)
 print (submatriz[i])
 i = i + 1

print 'La matriz es:'
print(x)
