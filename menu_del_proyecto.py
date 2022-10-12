from proyecto_2 import adivina
from proyecto_de_programacion import adiv_compu
from pr_pa_ti import pr_pa_ti2
from ahorcado import ahorcadohola
while True:

    print(
        "1. adivina un numero que te da la compu \n"
        "2.  piensa un numero y la compu lo adivinara \n"
        "3. piedra papel o tijera \n"
        "4. ahorcado \n"
        "5. Salir"
     )
    option = int(input(">>> "))
    if option == 1:
        adivina()
    elif option == 2:
        adiv_compu(100)
    elif option == 3:
        pr_pa_ti2()
    elif option == 4:
        ahorcadohola()
    elif option == 5:
        exit()

