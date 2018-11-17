 # Este es el juego de adivinar el número.

import random

intentosRealizados = 0
print('¡Hola! ¿Cómo te llamas?')

miNombre = input()

número = random.randint(1, 20)

print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:

    print('Intenta adivinar.')

    intento = input()

    intento = int(intento)

    intentosRealizados = intentosRealizados + 1
    if intento < número:

        print('El numero que has probado es muy bajo.')

    if intento > número:

         print('El numero que has probado es muy alto.')

    if intento == número:

        break

if intento == número:

     intentosRealizados = str(intentosRealizados)

     print('¡Buen trabajo, ' + miNombre + '! ¡Has adivinado el número en ' + intentosRealizados + ' intentos!')

if intento != número:

     número = str(número)

     print('Pues no. El número que estaba pensando era ' + número)
