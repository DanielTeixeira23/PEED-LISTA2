numeros = set()

for i in range(5):
    num = int(input(f"Digite o {i+1}° número: "))
    numeros.add(num)
    
novo = int(input('Escolha um dos números digitados para removê-lo: '))
if novo in numeros:
    numeros.remove(novo)
    print('Número removido.')
    print(numeros)
else:
    print('O número informado não está no conjunto.')