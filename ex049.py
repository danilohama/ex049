""" Refaça o exercicio 09 mostrando a tabuada de um número que o usuario escolher, contudo, agora utilizando um laço for
"""
num = int(input('Digite um número para saber sua tabuada: '))

for c in range(1, 11):
    print('{} X {} = {}'.format(num, c, num * c))
