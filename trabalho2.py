from collections import deque

class Grafo:
    def __init__(self, vertices, arestas, orientado=False):
        self.vertices = vertices
        self.orientado = orientado
        self.lista_adjacencia = {v: [] for v in vertices}
        
        # Construir lista de adjacência
        for aresta in arestas:
            u, v = aresta
            self.lista_adjacencia[u].append(v)
            if not orientado:
                self.lista_adjacencia[v].append(u)
    
    def bfs(self, vertice_inicial):
        """Executa BFS a partir de um vértice e retorna os vértices visitados"""
        visitados = set()
        fila = deque([vertice_inicial])
        visitados.add(vertice_inicial)
        
        while fila:
            atual = fila.popleft()
            for vizinho in self.lista_adjacencia[atual]:
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append(vizinho)
        
        return visitados
    
    def eh_conexo(self):
        """Verifica se o grafo é conexo"""
        if not self.vertices:
            return True
        
        # Executa BFS a partir do primeiro vértice
        visitados = self.bfs(self.vertices[0])
        
        # Se todos os vértices foram visitados, o grafo é conexo
        return len(visitados) == len(self.vertices)

def verificar_grafos():
    # 1- Verificar grafo não orientado
    print("=== GRAFO NÃO ORIENTADO ===")
    vertices_nao_orientado = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    arestas_nao_orientado = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x1'],
                            ['x4', 'x5'], ['x5', 'x6'], ['x6', 'x4']]
    
    grafo_nao_orientado = Grafo(vertices_nao_orientado, arestas_nao_orientado, orientado=False)
    conexo_nao_orientado = grafo_nao_orientado.eh_conexo()
    
    print(f"Vértices: {vertices_nao_orientado}")
    print(f"Arestas: {arestas_nao_orientado}")
    print(f"O grafo não orientado é conexo? {conexo_nao_orientado}")
    
    # Explicação do resultado
    if conexo_nao_orientado:
        print("✓ Todos os vértices estão conectados entre si.")
    else:
        print("✗ O grafo possui componentes desconexos.")
        # Mostrar componentes conexos
        componentes = encontrar_componentes_conexos(grafo_nao_orientado)
        print(f"Componentes conexos encontrados: {componentes}")
    
    print("\n" + "="*50 + "\n")
    
    # 2- Verificar grafo orientado
    print("=== GRAFO ORIENTADO ===")
    vertices_orientado = ['x1', 'x2', 'x3', 'x4', 'x5', 'x6']
    arcos_orientado = [['x1', 'x2'], ['x2', 'x3'], ['x3', 'x1'],
                      ['x4', 'x5'], ['x5', 'x6'], ['x2', 'x4']]
    
    grafo_orientado = Grafo(vertices_orientado, arcos_orientado, orientado=True)
    conexo_orientado = grafo_orientado.eh_conexo()
    
    print(f"Vértices: {vertices_orientado}")
    print(f"Arcos: {arcos_orientado}")
    print(f"O grafo orientado é conexo? {conexo_orientado}")
    
    # Explicação do resultado
    if conexo_orientado:
        print("✓ O grafo é fortemente conexo (existe caminho entre qualquer par de vértices).")
    else:
        print("✗ O grafo não é fortemente conexo.")
        # Verificar se é fracamente conexo
        fracamente_conexo = verificar_fracamente_conexo(grafo_orientado)
        print(f"O grafo é fracamente conexo? {fracamente_conexo}")

def encontrar_componentes_conexos(grafo):
    """Encontra todos os componentes conexos de um grafo"""
    visitados = set()
    componentes = []
    
    for vertice in grafo.vertices:
        if vertice not in visitados:
            componente = grafo.bfs(vertice)
            componentes.append(list(componente))
            visitados.update(componente)
    
    return componentes

def verificar_fracamente_conexo(grafo_orientado):
    """Verifica se um grafo orientado é fracamente conexo (conexo quando ignorada a orientação)"""
    # Criar versão não orientada do grafo
    vertices = grafo_orientado.vertices
    arestas_nao_orientadas = []
    
    for u in grafo_orientado.lista_adjacencia:
        for v in grafo_orientado.lista_adjacencia[u]:
            arestas_nao_orientadas.append([u, v])
    
    grafo_nao_orientado = Grafo(vertices, arestas_nao_orientadas, orientado=False)
    return grafo_nao_orientado.eh_conexo()

# Executar a verificação
if __name__ == "__main__":
    verificar_grafos()