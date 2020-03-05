from pprint import pprint
import random

def crear_tablero():
    tablero =[
        ['','','',],
        ['','','',],
        ['','','',],
    ]
    return tablero

def imprimir_triqui_pispirispis(tablero):
    for tab in tablero:
        print(tab)
        #for t in tab:

def llenar_tablero(tab_lleno):
    tab_lleno =[
       ['1','2','3',],
       ['4','5','6',],
       ['7','8','9',],
    ]
    return tab_lleno

def calentamiento():
    # lista de numeros que terminen en 9 o sean divisibles por 17 1037616822
    lista =  []
    for i in range(3000):
        if el_numero_es_valido(i):
            lista.append(i)
            #print(i)
    print(lista)       

def el_numero_es_valido(num):
    es_valido = num%17 == 0 or num%10 == 9
    return es_valido

def marcar_jugada():
    pass

def validar_jugada_maquina(num_bandera, tablero):
    while num_bandera == False:
        num=str(random.randint(1,9))
        for i in tablero:
            for n in range(len(i)):
                if i[n] != 'X' and i[n] != 'O' and i[n]== num:
                    num_bandera = True
                    #print (' !X !O ',num)
                    return num
                print('else ', num)

def validar_fin_juego(tablero):
    cont=0

    for i in range(len(tablero)):
        variable = tablero[i][0]
        for n in range(len(tablero[i])):
            if variable == tablero[i][n] :
                cont=cont+1
            else:
                cont=0
                break
        if cont == 3:
            if variable=='O':
                print('Perdiste')
            if variable=='X':
                print('Ganaste')
            return False
    if cont == 3 :
        if variable=='O':
            print('Perdiste')
        if variable=='X':
            print('Ganaste')
        return False
    cont = 0

    for i in range(len(tablero)):
        variable = tablero[i][0]
        for n in range(len(tablero[i])):
            if variable == tablero[n][i] :
                cont=cont+1
            else:
                cont=0
                break
        if cont == 3:
            return False
    if cont == 3 :
        return False

    cont = 0
    variable = tablero[0][0]
    for i in range(len(tablero)):
        
        if variable == tablero[i][i] :
            cont=cont+1
        else:
            cont=0
            break
    if cont == 3 :
        if variable=='O':
            print('Perdiste')
        if variable=='X':
            print('Ganaste')
        return False
    else: 
        return True
        
    for i in range(len(tablero)):
        variable = tablero[i][0]
        for n in range(len(tablero[i])):
            if variable == tablero[n][i] :
                cont=cont+1
            else:
                cont=0
                break
        if cont == 3:
            if variable=='O':
                print('Perdiste')
            if variable=='X':
                print('Ganaste')
            return False
    if cont == 3 :
        if variable=='O':
            print('Perdiste')
        if variable=='X':
            print('Ganaste')
        return False
    else: 
        return True


def main():
    print("Vamos a jugar")
    print("El jugador sera representado con la X")
    print("La maquina sera representado con la O")
    #calentamiento();
    tab_juego = crear_tablero()
    imprimir_triqui_pispirispis( tab_juego )
    tablero_lleno = llenar_tablero(tab_juego)
    imprimir_triqui_pispirispis(tablero_lleno)
    juego_terminado = True
    while juego_terminado == True :
        jugada_x = input("ingrese poscion en x: ")
        for i in tablero_lleno:
            for n in range(len(i)):
                if jugada_x == i[n]:
                    i[n]='X'
                    break

        imprimir_triqui_pispirispis(tablero_lleno)
        jugada_y = validar_jugada_maquina(False, tablero_lleno)
        print("ingrese poscion en y:", jugada_y)
        for i in tablero_lleno:
            for n in range(len(i)):
                if jugada_y == i[n]:
                    i[n]='O'
                    break
        imprimir_triqui_pispirispis(tablero_lleno)
        juego_terminado = validar_fin_juego(tablero_lleno)


if __name__ == "__main__":
    main()

