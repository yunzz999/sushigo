
puntaje1,puntaje2,puntaje3,puntaje4,puntaje5 = 0,0,0,0,0

x=1

while True:
    print("ronda",x)
    puntaje1+=int(input("puntaje jugador1:\t"))
    

    if x ==5:
        break
    else:
        x+=1
print(puntaje1)
