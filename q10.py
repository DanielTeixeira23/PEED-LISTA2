grafo = {}

num_vertices = int(input('Digite a quantidade de vértices do grafo: '))
for i in range(num_vertices):
    vertice = input(f"Digite o {i+1}° vértice: ")
    grafo[vertice] = []
    
num_arestas = int(input('Digite a quantidade de arestas: '))
for i in range(num_arestas):
    a, b = input(f"Digite vértices que formam a {i+1}ª aresta: ").split()
    grafo[a].append(b)
    grafo[b].append(a)

a, b = input('Digite uma das arestas para ser removida: ').split()
if a in grafo and b in grafo:
    grafo[a].remove(b)
    grafo[b].remove(a)
    print('Aresta removida.')
else:
    print('Aresta não encontrada.')
    
print(grafo)