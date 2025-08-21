import random
def eh_conexo(grafo):
    origem = random.choice(list(grafo.keys()))
    visitados = fecho_transitivo(grafo, origem)
    return visitados == set(grafo.keys())

def criar_lista_de_adjacencia(vertices, arestas):
    lista_de_adjacencia = {vertice: [] for vertice in vertices}
    for v1, v2 in arestas:
        lista_de_adjacencia[v1].append(v2)
        lista_de_adjacencia[v2].append(v1)
    return lista_de_adjacencia

def criar_lista_de_adjacencia_direcionado(vertices, arcos):
    grafo = {v: [] for v in vertices}
    for u, v in arcos:
        grafo[u].append(v)   # só adiciona u → v
    return grafo

def fecho_transitivo(grafo, origem):
    visitados = set()
    def dfs(v):
        if v in visitados:
            return
        visitados.add(v)
        for vizinho in grafo[v]:
            dfs(vizinho)
    dfs(origem)
    return visitados

def simetrizar_grafo(grafo):
    # cria uma cópia para não alterar o original
    grafo_simetrico = {v: set(vizinhos) for v, vizinhos in grafo.items()}
    
    for u in grafo:
        for v in grafo[u]:
            # adiciona o arco simétrico v → u
            grafo_simetrico[v].add(u)
    
    # converte de volta para listas (se preferir consistência com sua função anterior)
    return {v: list(vizinhos) for v, vizinhos in grafo_simetrico.items()}

def sucessores(grafo, origem):
    visitados = set()

    def dfs(v):
        for vizinho in grafo[v]:
            if vizinho not in visitados:
                visitados.add(vizinho)
                dfs(vizinho)

    dfs(origem)
    return visitados

def lista_de_sucessores(grafo):
    return {v: sucessores(grafo, v) for v in grafo}

vertices = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']

arestas = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x1'],
           ['x4', 'x5'], ['x5', 'x6'], ['x6', 'x4']]

arcos = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x1'],
           ['x4', 'x5'], ['x5', 'x6'], ['x2', 'x4']]


grafo = criar_lista_de_adjacencia(vertices, arestas)
grafo2 = criar_lista_de_adjacencia_direcionado(vertices, arcos)
grafo3 = simetrizar_grafo(grafo2)
