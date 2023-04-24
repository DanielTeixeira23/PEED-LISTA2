dict = {}

num = int(input('Quantas chaves vão ser adicionadas ao dicionário: '))
print('\n')
for i in range(num):
    chave = input('Digite uma chave para esse dicionário: ')
    valor = input('Digite um valor para essa chave: ')
    dict[chave] = valor
    
if 'profissão' in dict:
    print('A chave profissão está presente no dicionário.')
else:
    print('A chave profissão não está presente no dicionário.')
    
