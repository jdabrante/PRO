gamer1 = "Jugador 1"
gamer2 = "Jugador 2"
person1 = "papel"
person2 = "tijera"
paper = person1=="papel" and person2=="piedra"
scissors = person1=="tijera" and person2=="papel"
stone = person1=="piedra" and person2=="papel"
if  paper or scissors or stone:
    win=gamer1
else: 
    win=gamer2

print(f'Gana el jugador {win}')