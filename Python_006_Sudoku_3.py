import math

dim = 4
d = {}

i = 1
j = 1
while i <= dim:
    while j <= dim:
        vble = str(i) + str(j)
        d[vble] = range(1, dim + 1)
        j += 1
    
    j = 1
    i += 1

print "Comprobamos la longitud del dic:"
print d

print "Comprobamos el elemento 13:"
print d["13"]

print "Le quitamos un elemento a 13:"
d["13"].pop()
print d["13"]

print "Le anadimos un elemento a 13:"
d["13"].append(5)
print d["13"]

print "Le quitamos un elemento a 13 (el 5):"
d["13"].remove(5)
print d["13"]


def PerteneceAcuadricula(coordenada):
    r_dim = math.sqrt(dim)
    print "Coordenada: " + coordenada
    c_x = (int(coordenada[0]) + 1) // r_dim 
    c_y = (int(coordenada[1]) + 1) // r_dim
    print "Pertenece a x:", c_x, "- y:", c_y
    print ""
    
PerteneceAcuadricula("13")
PerteneceAcuadricula("11")
PerteneceAcuadricula("14")
PerteneceAcuadricula("44")
PerteneceAcuadricula("24")
