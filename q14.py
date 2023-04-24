numeros = set()

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.add(num)

for num in numeros:
    if num==3:
        print('O número 3 está no conjunto.')
        break
else:
    print('O número 3 não está no conjunto.')