 # Este es el juego de adivinar el número.
import tkinter as tk
from tkinter import simpledialog
import random

intentosRealizados = 0
print('¡Hola! ¿Cómo te llamas?')

miNombre = input()

número = random.randint(1, 20)
print(número)

print('Bueno, ' + miNombre + ', estoy pensando en un número entre 1 y 20.')

while intentosRealizados < 6:
    
    application_window = tk.Tk()

    intento = simpledialog.askinteger("Input", "Introduce numero: ",
                                 parent=application_window,
                                 minvalue=1, maxvalue=20)


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
