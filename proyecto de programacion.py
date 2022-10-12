import random

def adiv(x):
    numero_random=random.radiant(1,x)
    adiv=0
    while adiv != numero_random:
        adiv= int(input(f'un numero entre 1 y {x}'))
        if adiv<numero_random:
            print("adivina de nuevo muy bajo")
        elif numero_random>adiv:
            print("adivina de nuevo muy alto")

print("adivine tu numero")

def adiv_compu(x):
    bajo=1
    alto=x
    dev=''
    while dev != "1":
        adiv