import random
import math
from proyecto_2 import adivina
from proyecto_de_programacion import adiv_compu
while True:

    print(
        "1. \n"
        "2. \n"
        "*. Salir"
     )
    option = int(input(">>> "))
    if option == 1:
        adiv_compu(100)
    elif option == 2:
        adivina()
        print("hola")