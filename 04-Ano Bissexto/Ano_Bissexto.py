#ex de ano bissexto a partir do ano que o usuário digitar

from datetime import date
from time import sleep
ano = int(input('Qual ano você quer analisar? Coloque 0 para analisar o ano atual: '))
if ano == 0:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'Analisando o ano {ano}...')
    sleep(2)
    print(f'O ano {ano} é bissexto! ')
else:
    print(f'Analisando o ano {ano}...')
    sleep(2)
    print(f'O ano {ano} não é bissexto!')