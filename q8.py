dict = {}

num = int(input('Quantas chaves vão ser adicionadas ao dicionário: '))
for i in range(num):
    chave = input('Digite uma chave para esse dicionário: ')
    valor = input('Digite um valor para essa chave: ')
    dict[chave] = valor

if 'idade' in dict:
    print('O valor da chave idade é:', dict['idade'])
else:
    print('O valor da chave idade não foi encontrada.')