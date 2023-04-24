par = []

for i in range(10):
    num = int(input(f"Digite o {i}° número: "))
    par.append(num)

print('Os números digitados nos índices pares foi: ')
for i in range(len(par)):
    if i%2==0:
        print(par[i])