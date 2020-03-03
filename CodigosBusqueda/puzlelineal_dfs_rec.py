# Puzle lineal con busqueda en profundidad recursiva
from arbol import Nodo

def buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados):
    visitados.append(nodo_inicial.get_datos())
    if nodo_inicial.get_datos() == solucion:
        # Solucion encontrada
        return nodo_inicial
    else:
        #Expandir nodos hijos
        dato_nodo = nodo_inicial.get_datos()

        #Operador izquierdo
        hijo = [dato_nodo[1], dato_nodo[0], dato_nodo[2], dato_nodo[3]]
        hijo_izquierdo = Nodo(hijo)
        
        #Operador central
        hijo = [dato_nodo[0], dato_nodo[2], dato_nodo[1], dato_nodo[3]]
        hijo_central = Nodo(hijo)
        
        #Operador derecha
        hijo = [dato_nodo[0], dato_nodo[1], dato_nodo[3], dato_nodo[2]]
        hijo_derecho = Nodo(hijo)
        
        nodo_inicial.set_hijos([hijo_izquierdo, hijo_central, hijo_derecho])
        
        for nodo_hijo in nodo_inicial.get_hijos():
            if not nodo_hijo.get_datos() in visitados:
                # Llamada recursiva
                sol = buscar_solucion_DFS_rec(nodo_hijo, solucion, visitados)
                if sol != None:
                    return sol
        return None
            

def main():
    estado_inicial = [4,2,3,1]
    solucion = [1, 2, 3, 4]
    nodo_solucion = None
    visitados = []
    nodo_inicial = Nodo(estado_inicial)
    nodo_solucion = buscar_solucion_DFS_rec(nodo_inicial, solucion, visitados)
    
    #Mostrar resultado
    resultado = []
    nodo = nodo_solucion
    while nodo.get_padre() != None:
        resultado.append(nodo.get_datos())
        nodo = nodo.get_padre()
    resultado.append(estado_inicial)
    resultado.reverse()
    print(resultado)


if __name__ == '__main__':
    main()