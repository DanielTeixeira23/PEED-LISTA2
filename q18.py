dados = {}

num = int(input('Quantas chaves serão adicionadas: '))
for i in range(num):
    chaves = input('Digite uma chave: ')
    valores = input('Digite um valor: ')
    dados[chaves] = valores
    
nova_chave = input('Digite a cidade onde você nasceu: ')
dados['Cidade'] = nova_chave

print(dados)