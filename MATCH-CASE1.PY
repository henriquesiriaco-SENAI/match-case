import os
os.system('cls')

genero = input('Digite seu genero M = masculino ou F = feminino: ').upper()
peso = float(input('digite seu peso: '))
altura = float(input('digite sua altura: '))

match genero:
    case  'M':
        print('\n')
        print ('genero masculino')
        print (f'sua altura é: {altura}')
        print (f'seu peso: {peso}')
        print(f'peso ideal {(72.7 * altura) - 58}')

    case 'F':
        print('\n')
        ('genero feminino')
        print (f'sua altura é: {altura}')
        print (f'seu peso: {peso}')
        print(f'peso ideal {(62.1 * altura) - 44.7}')
        exit()

    case _:
        print('opção invalida')
        exit()