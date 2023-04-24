lista = []

for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    lista.append(nome)

nome_lista = input('Escolha um dos nomes digitados para substituí-lo: ')
if nome_lista in lista:
    indice = lista.index(nome_lista)
    novo_nome = input('Digite o novo nome: ')
    lista[indice] = novo_nome
else:
    print('O nome informado não está na lista.')
    
nomes = tuple(lista)
print(nomes)