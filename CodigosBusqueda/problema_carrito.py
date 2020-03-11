# viaje lineal por carretera con busqueda de coste uniforme
import math
from functools import cmp_to_key
from arbol import Nodo



if __name__ == '__main__':

    estado_inicial = [0,0]
    solucion = [5,3]
    tamano=[10,10]
    nodo_solucion = buscar_solucion_UCS(tamano, estado_inicial, solucion)
    #Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)
    print("Coste:", str(nodo_solucion.get_coste()))

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera =[]
    nodoInicial = Nodo(estado_inicial)
    nodoInicial.set_coste(0)
    nodos_frontera.append(nodoInicial)
    while (not solucionado) and len(nodos_frontera) != 0:
        # Ordenar la lista de nodos frontera
        nodos_frontera = sorted(nodos_frontera, key=cmp_to_key(compara))
        nodo = nodos_frontera[0]
        # Extraer nodo y añadirlo a visitados
        nodos_visitados.append(nodos_frontera.pop(0))
        if nodo.get_datos() == solucion:
            # Solucion encontrada
            solucionado=True
            return nodo
        else:
            #Expandir nodos hijos (ciudades con conexión)
            dato_nodo = nodo.get_datos()

            lista_hijos = []
            lista_posibles_hijos = procrear(nodoInicial,conexiones,solucion )
            for un_hijo in lista_posibles_hijos[dato_nodo]:
                hijo = Nodo(un_hijo)
                #Cálculo g(n)
                if celda_valida(hijo):
                    coste = 2
                    hijo.set_coste(nodo.get_coste() + coste)
                    lista_hijos.append(hijo)
                    if not hijo.en_lista(nodos_visitados):
                        # Si está en la lista lo sustituimos con el 
                        # nuevo valor de coste si es menor
                        if hijo.en_lista(nodos_frontera):
                            for n in nodos_frontera:
                                if n.igual(hijo) and n.get_coste() > hijo.get_coste():
                                    nodos_frontera.remove(n)
                                    nodos_frontera.append(hijo)
                        else:
                            nodos_frontera.append(hijo)

            nodo.set_hijos(lista_hijos)
def compara(x, y):
    '''# g(n) + h(n) para ciudad x
    lat1 = coord[x.get_datos()][0]
    lon1 = coord[x.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]
    d = int(geodist(lat1, lon1, lat2, lon2))
    c1 = x.get_coste() + d

    # g(n) + h(n) para ciudad y
    lat1 = coord[y.get_datos()][0]
    lon1 = coord[y.get_datos()][1]
    lat2 = coord[solucion][0]
    lon2 = coord[solucion][1]
    d = int(geodist(lat1, lon1, lat2, lon2))
    c2 = y.get_coste() + d
    return c1 - c2'''
    pass

def procrear(inicial,coordenada, matriz):
    coord=[[0,1], [1,0],[1,1],[0,-1],[-1,0],[-1,-1]]
    posibles_coordenadas=[]
    for i in coordenada:
        if coordenada[0] < matriz[0] and coordenada[1]< matriz[1]:
            if coordenada[0]+coord[0] > 0 and coordenada[1]+coord[1]>0:
                posibles_coordenadas.append(i)

    '''
    if matriz[inicial[0]+1]>0 and matriz[inicial[1]+1]>0:
        x.append(matriz[inicial[0]+1])
        x.append(matriz[inicial[1]+1])
        posibles_coordenadas.append(x)
    if matriz[inicial[0]+1]>0:
        x.append(matriz[inicial[0]+1])
        x.append(matriz[inicial[1]])
        posibles_coordenadas.append(x)
    if  matriz[inicial[1]+1]>0:
        x.append(matriz[inicial[0]])
        x.append(matriz[inicial[1]+1])
        posibles_coordenadas.append(x)
    if matriz[inicial[0]-1]>0 and matriz[inicial[1]-1]>0:
        x.append(matriz[inicial[0]+1])
        x.append(matriz[inicial[0]+1])
        posibles_coordenadas.append(x)
    if matriz[inicial[0]-1]>0:
        x.append(matriz[inicial[0]+1])
        x.append(matriz[inicial[0]+1])
        posibles_coordenadas.append(x)
    if  matriz[inicial[1]-1]>0:
        x.append(matriz[inicial[0]+1])
        x.append(matriz[inicial[0]+1])
        posibles_coordenadas.append(x)
    return posibles_coordenadas
    '''
    return posibles_coordenadas


def celda_valida(posible_coordenada):
    if (posible_coordenada[0]+posible_coordenada[1])%3 != 0:
        return True
    else:
        return False



 


