import random



def adiv_compu(x):
    bajo = 1
    alto = x
    dev=''
    while dev != "c":
        if bajo != alto:
            adiv = random.randint(bajo,alto)
        else:
            adiv = bajo
        adiv = random.randint(bajo,alto)
        dev=input(f'es {adiv} muy alto(a),muy bajo(b) o correcto(c)').lower()
        if dev == "a":
            alto = adiv - 1
        elif dev == "b":
            bajo = adiv + 1
    print("la computadora adivino tu numero correctamente")

adiv_compu(100)