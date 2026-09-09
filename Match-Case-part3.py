import os
os.system('cls')

print('=========== Menu ==========')
print('\n 1 - picanha R$:25,00')
print('\n 2 - lasanha R$:20,00')
print('\n 3 - strogonoof R$:18,00')
print('\n 4 - bife acebolado R$15:00')
print('\n 5 - pão com ovo R$:5,00')

escolha = int(input('\n Escolha o seu pedido: '))

match escolha:
    case 1:
        print ('picanha')
    case 2:
        print('lasanha')
    case 3:
        print('lasanha')
    case 4:
        print('bife acebolado')
    case 5:
        print('pão com ovo')