
# viaje lineal por carretera con busqueda de coste uniforme
from functools import cmp_to_key
from arbol import Nodo

class NodoReload(Nodo):
    def __init__(self, *args):
        super(NodoReload, self).__init__(*args)
        self.set_hijos()

        #super(NodoReload, self).set_hijos()

    def set_hijos(self):
        pass


def compara(x, y):
    return x.get_coste() - y.get_coste()

def buscar_solucion_UCS(conexiones, estado_inicial, solucion):
    solucionado = False
    nodos_visitados = []
    nodos_frontera =[]
    nodoInicial = Nodo(estado_inicial)
    nodoInicial.set_coste(0)
    nodos_frontera.append(nodoInicial)
    #print(nodos_frontera)
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
            for un_hijo in conexiones[dato_nodo]:
                hijo = Nodo(un_hijo)
                coste = conexiones[dato_nodo][un_hijo]
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
            #print(lista_hijos)

def main():
    conexiones = {
        'Malaga': {'Granada': 125, 'Madrid': 513,},
        'Sevilla': {'Madrid': 514},
        'Granada': {'Malaga': 125, 'Madrid': 423, 'Valencia': 421},
        'Valencia': {'Granada': 491, 'Madrid': 356, 'Zaragoza': 309, 
            'Barcelona': 346,},
        'Madrid': {'Salamanca': 203, 'Sevilla': 514, 'Malaga': 513, 
            'Granada': 423, 'Barcelona': 603, 'Santander': 437, 'Valencia': 356,
            'Zaragoza': 313,  'Santiago': 599},
        'Salamanca': {'Santiago': 390, 'Madrid': 203},
        'Santiago': {'Salamanca': 390, 'Madrid': 599},
        'Santander': {'Madrid': 437, 'Zaragoza': 394},
        'Zaragoza': {'Barcelona': 296, 'Valencia': 309, 'Madrid': 313},
        'Barcelona': {'Zaragoza': 296, 'Madrid': 603, 'Valencia': 346}
    }
    estado_inicial = 'Malaga'
    solucion = 'Santiago'
    nodo_solucion = buscar_solucion_UCS(conexiones, estado_inicial, solucion)
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


if __name__ == '__main__':
    main()