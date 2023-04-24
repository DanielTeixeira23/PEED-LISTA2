grafo = {}

num_vertices = int(input('Digite a quantidade de vértices do grafo: '))
for i in range(num_vertices):
    vertice = input(f"Digite o {i+1}° vértice: ")
    grafo[vertice] = []
    
num_arestas = int(input('Digite a quantidade de arestas do grafo: '))
for i in range(num_arestas):
    a, b = input(f"Digite os vértices que formam o {i+1}ª aresta: ").split()
    grafo[a].append(b)
    grafo[a].append(a)

if 'C' in grafo['A']:
    print('A aresta A C está presente no grafo.')
else:
    print('A aresta A C não está presente no grafo.')
    
print(grafo)