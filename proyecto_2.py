
import random
import math
def adivina():
    bajo = int(input("pon un numero entre:- "))
    alto = int(input("y:- "))
    x = random.randint(bajo, alto)
    print("\n\tsolo tienes ",
          round(math.log(alto - bajo + 1, 2)),
          " chances de adivinar el entero\n")
    cont = 0
    while cont < math.log(alto - bajo + 1, 2):
        cont += 1
        adivina = int(input("adivina un nnumero:- "))
        if x == adivina:
            print("Felicidades lo hiciste en tu ",
                  cont, " intento")
        elif x > adivina:
            print("adivinaste demasiado bajo!")
        elif x < adivina:
            print("adivinaste demasiado alto!")
    if cont >= math.log(alto - bajo + 1, 2):
        print("\nel numero es %d" % x)
        print("\tmejor suerte la proxima vez!")