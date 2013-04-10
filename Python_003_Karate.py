#Karate
import random
vidas_jugador_1 = 3
vidas_jugador_2 = 3
bucle = 0

def lee_teclado():
 ataque = input('Ataque j.1: alto(1), medio(2), bajo(3)')
 defensa = input ('Defensa j.1: alto(1), medio(2), bajo(3)')
 return ataque, defensa
 
while True:
 bucle = bucle + 1
 ataque_jugador_1, defensa_jugador_1 = lee_teclado()
 ataque_jugador_2 = random.randint(1,3)
 defensa_jugador_2 = random.randint(1,3)
 
 #Combate
 if ataque_jugador_1 != defensa_jugador_2:
  print ('Golpe del jugador 1. Jugador 2 pierde una vida!')
  vidas_jugador_2 = vidas_jugador_2 - 1
 else:
  print ('Jugador 2 ha parado el golpe!')     

 if ataque_jugador_2 != defensa_jugador_1:
  print ('Golpe del jugador 2. Jugador 1 pierde una vida!')
  vidas_jugador_1 = vidas_jugador_1 - 1
 else:
  print ('Jugador 1 ha parado el golpe!')     

 if (vidas_jugador_1 == 0) and (vidas_jugador_2 == 0):
  print ('KO Doble')
  break
 
 if (vidas_jugador_1 == 0):
  print ('Jugador 1 está KO')
  break

 if (vidas_jugador_2 == 0): 
  print ('Jugador 2 está KO')
  break

print ('Se acabó el combate!')
print ('Rondas: ' + str(bucle))
