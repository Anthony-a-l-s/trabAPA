def criar_lista_de_adjacencia(vertices, arestas):
    lista_de_adjacencia = {vertice: [] for vertice in vertices}

    for v1, v2 in arestas:
        lista_de_adjacencia[v1].append(v2)
        lista_de_adjacencia[v2].append(v1)

    return lista_de_adjacencia


vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']

arestas = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x1'],
           ['x4', 'x5'], ['x5', 'x6'], ['x6', 'x4']]

lista_de_adjacencia = criar_lista_de_adjacencia(vertices, arestas)

print(lista_de_adjacencia)