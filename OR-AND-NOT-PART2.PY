import os
from datetime import date
os.system('cls')

matricula = input('Digite a sua matricula: ')
idade = int(input('Sua idade'))
tempo_de_trabalho = int(input('começou a trabalha: '))


tempo = date.today().year - tempo_de_trabalho

if idade >= 65 or tempo >= 30:
    resultado = ('Requer aposentadoria')
else:
    resultado = ('Não requer aposentadoria')

print(f'Codigo {matricula}')
print(f'idade {idade}')
print(f'esteve conosco por: {tempo} anos')
print(f'Resultado: {resultado}')
print(f'data: {date.today()}')