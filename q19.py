numeros = set()

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.add(num)
    
total = len(numeros)    

print(f"O conjunto tem {total} elementos.")