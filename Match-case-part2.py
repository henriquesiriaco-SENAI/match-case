import os
os.system('cls')

dia = int(input('Número 1 a 7: '))
match dia:
    case 1 :
        print('hoje é segundada-feira')
    case 2:
        print('hoje é terça-feira')
    case 3:
        print('hoje é quarta-feira')
    case 4:
        print('hoje é quinta-feira')
    case 5:
        print('hoje é sexta-feira')
    case 6|7 :
        print('hoje é fim de semana')
    case _:
        print('dia invalido')