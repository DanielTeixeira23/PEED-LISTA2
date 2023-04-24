lista = []

print('Digite 5 números\n')
for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    lista.append(num)

x = int(input('Digite mais um número: '))
lista.append(x)

print(lista)