import random

def pr_pa_ti2():
    com=random.randint(1,3)

    vos=input("elije piedra papel o tijeras\n >>>")
    if vos=="piedra" and com==3:
        print("tijeras")
        print("ganaste")
    if vos=="piedra" and com==2:
        print("papel")
        print("perdiste")
    if vos=="piedra" and com==1:
        print("tijeras")
        print("empataste")
    if vos=="papel" and com==3:
        print("tijeras")
        print("perdiste")
    if vos=="papel" and com==2:
        print("papel")
        print("empataste")
    if vos=="papel" and com==1:
        print("piedra")
        print("ganaste")
    if vos=="tijeras" and com==3:
        print("tijeras")
        print("empataste")
    if vos=="tijeras" and com==2:
        print("papel")
        print("ganaste")
    if vos=="tijeras" and com==1:
        print("piedra")
        print("perdiste")