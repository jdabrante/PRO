edad = int(input('Dame tu edad: '))
peso = int(input('Dame tu peso: '))
pulsaciones = int(input('Dame tu pulso: '))
plaquetas = int(input('Dame tu número de plaquetas: '))
requisitos = ""

if (edad >= 18 and edad <= 65) and (peso >= 55) and (pulsaciones >= 50 and pulsaciones <= 110) and (plaquetas > 150_000):
    requisitos = 'Eres apto'
else: 
    requisitos= 'No eres apto'

print(requisitos)