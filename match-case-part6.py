import os
os.system('cls')

dia = int(input('Sua forma de pagamento sera prazo ou a vista (1/2):'))
vista = 1
prazo = 2
valor = 100
desconto = valor * 0.10

match dia:
    case 1:
        print ('valor do produto R$ 100')
        print ('forma de pagamento à vista')
        print ('desconto de 10%')
        print (f'desconto {valor - desconto}')
match dia:
    case 2:
        print('valor do produto R$100')
        parcela = int(input('digite quantas parcelas: '))
         if quantidade_parcelas > 6:
            print('Quantidade de parcelas inválida.')
             exit()
        print(f'quantidade de parcelas:{parcela}')
        print(f'seu parcela será de: {valor / parcela}')
        print('valor total R$ 100')
