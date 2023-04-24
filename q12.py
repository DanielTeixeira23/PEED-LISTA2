lista = []

for i in range(3):
    nome = input(f"Digite o {i+1}° nome: ")
    lista.append(nome)

nova_tupla = tuple(lista)

for j in range(len(nova_tupla)): 
    if nova_tupla[j].lower() == 'maria':
        print('O nome Maria está na lista')
        break
else:
    print('O nome Maria não foi digitado.')