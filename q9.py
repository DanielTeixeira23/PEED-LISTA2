numeros = set()

for i in range(10):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.add(num)
    
for num in numeros.copy():
    if num%2==0:
        numeros.remove(num)

print(numeros)