#5Penalties
import random
goles_equipo_1 = 0
goles_equipo_2 = 0

print ("Coooooomienza el partido")
for x in range (1 ,5):
 portero_1 = random.randint(1,10)
 portero_2 = random.randint(1,10)
 
 delantero_1 = random.randint(1,10)
 delantero_2 = random.randint(1,10)    
 
 #Lanzamiento de penaltis
 if delantero_1 >= portero_1:
  print ('Gol del equipo 1!')
  goles_equipo_1 = goles_equipo_1 + 1

 if delantero_2 >= portero_2:
  print ('Gol del equipo 2!')
  goles_equipo_2 = goles_equipo_2 + 1

print ('Se acabó el partido! Resultado:')    
print ('Equipo 1: ' + str(goles_equipo_1))
print ('Equipo 2: ' + str(goles_equipo_2))
