import os
os.system('cls')

genero = input('Digite H para homem ou M para mulher: ').upper()
nascimento = int(input('seu nascimento: '))
idade = 2026 - nascimento


if genero ==  'H' and  idade >= 18:
    print('bem vindo ao exercito soldado')
else:
    print('você não esta qualificado(a)')