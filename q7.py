numeros = []

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.append(num)
    
a = tuple(numeros)

print('O primeiro elemento da tupla é:', a[0])