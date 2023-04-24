lista = []
cont = 0

for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    lista.append(nome)

nova_tupla = tuple(lista)

for j in range(len(nova_tupla)):
    if nova_tupla[j].lower() == 'maria':
        cont+=1
print(f"O nome Maria foi digitado {cont} vezes.")