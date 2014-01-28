#!/usr/local/bin/python3

# funcion a la que paso un candidato y debe comprobar que:
#   num - 1 % 2 == 0
#   num - 2 % 3 == 0
#   ...
#   num - 11 % 12 == 0
def compruebaSegundaCondicion(num):
  for x in range(1, 12):
    if ((num - x) % (x + 1) != 0):
      break
    if (x == 11):
      print ("Este es el numero: " + str(num))

# empiezo la busqueda del numero
array_candidatos = []
for num in range(0, 99999):
    array_num = ['0','0','0','0','0']
    num_str = str(num)
    # relleno el array con la forma: ['1','2','3','4','5']
    for x in range(0, len(num_str)):
        array_num[(len(array_num) - 1) - x] = num_str[(len(num_str) - 1) - x]

    # si los 5 numeros son distintos, es un posible candidato    
    if (5 == len(set(array_num))):
        array_candidatos.append(num)
        
print ("El numero de candidatos es: " + str(len(array_candidatos)))

# compruebo los candidatos
for num in array_candidatos:
  compruebaSegundaCondicion(num)
