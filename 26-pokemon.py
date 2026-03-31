import os
os.system ("cls")

turno = 1
pokemon_1 = 100
pokemon_2 = 100
while pokemon_1 or pokemon_2 > 0:
    print("\nTurno", turno)
    print("Vida Jogador 1:", pokemon_1)
    print("Vida Jogador 2:", pokemon_2)
    
    ação = int(input("jogador um vai fazer oque 1-atacar 2-curar 3-fugir"))
    
    if ação == 1: 
     pokemon_2 -= 10
    elif ação == 2:
     pokemon_1 += 5
    elif ação == 3:
     pokemon_1 = 0
     if pokemon_2 <= 0:
        break
    ação_2 = int(input("jogador dois vai fazer oque 1-atacar 2-curar 3-fugir"))
    if ação_2 == 1: 
     pokemon_1 -= 10
    elif ação_2 == 2:
     pokemon_2 += 5
    elif ação_2 == 3:
     pokemon_2 -= 100

     turno += 1

if pokemon_1 <= 0 and pokemon_2 <= 0:
    print("Empate!")
elif pokemon_1 <= 0:
    print("Jogador 2 venceu!")
else:
    print("Jogador 1 venceu!")
    
 
   