import os
import time

def two():
    x=1
    puntajes = {'jugador 1':0,'jugador 2':0}
    for i in range(1,6):
        print("\tRonda",i,'\n') #mejorar esta interfaz
        puntajes['jugador 1']+=int(input("puntaje jugador 1:\t"))
        puntajes['jugador 2']+=int(input("puntaje jugador 2:\t"))
        os.system('clear')
        print('\n\t\tTabla de posiciones\n')
        print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'])
        time.sleep(5)
        os.system('clear')

    print('El ganador es',max(puntajes),'!!!') 
    print('\n\t\tTabla de posiciones Final\n')
    print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'])

def three():
    x=1
    puntajes = {'jugador 1':0,'jugador 2':0,'jugador 3':0}
    for i in range(1,6):
        print("\tRonda",i,'\n') #mejorar esta interfaz
        puntajes['jugador 1']+=int(input("puntaje jugador 1:\t"))
        puntajes['jugador 2']+=int(input("puntaje jugador 2:\t"))
        puntajes['jugador 3']+=int(input("puntaje jugador 3:\t"))
        os.system('clear')
        print('\n\t\tTabla de posiciones\n')
        print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'],'\nJugador 3:',puntajes['jugador 3'])
        time.sleep(5)
        os.system('clear')

    print('El ganador es',max(puntajes),'!!!') 
    print('\n\t\tTabla de posiciones Final\n')
    print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'],'\nJugador 3:',puntajes['jugador 3'])

def four():
    x=1
    puntajes = {'jugador 1':0,'jugador 2':0,'jugador 3':0,'jugador 4':0}
    for i in range(1,6):
        print("\tRonda",i,'\n') #mejorar esta interfaz
        puntajes['jugador 1']+=int(input("puntaje jugador 1:\t"))
        puntajes['jugador 2']+=int(input("puntaje jugador 2:\t"))
        puntajes['jugador 3']+=int(input("puntaje jugador 3:\t"))
        puntajes['jugador 4']+=int(input("puntaje jugador 4:\t"))
        os.system('clear')
        print('\n\t\tTabla de posiciones\n')
        print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'],'\nJugador 3:',puntajes['jugador 3'],'\nJugador 4:',puntajes['jugador 4'])
        time.sleep(5)
        os.system('clear')

    print('El ganador es',max(puntajes),'!!!') 
    print('\n\t\tTabla de posiciones Final\n')
    print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'],'\nJugador 3:',puntajes['jugador 3'],'\nJugador 4:',puntajes['jugador 4'])

def five():
    x=1
    puntajes = {'jugador 1':0,'jugador 2':0,'jugador 3':0,'jugador 4':0,'jugador 5':0}
    for i in range(1,6):
        print("\tRonda",i,'\n') #mejorar esta interfaz
        puntajes['jugador 1']+=int(input("puntaje jugador 1:\t"))
        puntajes['jugador 2']+=int(input("puntaje jugador 2:\t"))
        puntajes['jugador 3']+=int(input("puntaje jugador 3:\t"))
        puntajes['jugador 4']+=int(input("puntaje jugador 4:\t"))
        puntajes['jugador 5']+=int(input("puntaje jugador 5:\t"))
        os.system('clear')
        print('\n\t\tTabla de posiciones\n')
        print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'],'\nJugador 3:',puntajes['jugador 3'],'\nJugador 4:',puntajes['jugador 4'],'\nJugador 5:',puntajes['jugador 5'])
        time.sleep(5)
        os.system('clear')

    print('El ganador es',max(puntajes),'!!!') 
    print('\n\t\tTabla de posiciones Final\n')
    print('Jugador 1:',puntajes['jugador 1'],'\nJugador 2:',puntajes['jugador 2'],'\nJugador 3:',puntajes['jugador 3'],'\nJugador 4:',puntajes['jugador 4'],'\nJugador 5:',puntajes['jugador 5'])

def menu():
    os.system('clear')
    print ("Elige la cantidad de Jugadores")
    print ("\t1 - 2 Jugadores")
    print ("\t2 - 3 Jugadores")
    print ("\t3 - 4 Jugadores")
    print ("\t4 - 5 Jugadores")
    print ("\t9 - salir")
 

while True:
    os.system('clear')
    menu()
    
    opcionMenu = int(input("inserta un numero valor >> "))

    if opcionMenu==1:
        two()
    if opcionMenu==2:
        three()
    if opcionMenu==3:
        four()
    if opcionMenu==4:
        five()
    if opcionMenu==9:
        break
    else:
        print('ingrese un dato valido')
        time.sleep(1)

