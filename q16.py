lista = []

for i in range(10):
    num = int(input(f"Digite o {i+1}° número: "))
    lista.append(num)

novaLista = []

for num in lista:
    mult = num*2
    novaLista.append(mult)
    
print(novaLista)