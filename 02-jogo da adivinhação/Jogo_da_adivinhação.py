# faça um programa que o computador escolha um nuumero inteiro e o usuário
# tente adivinhar qual foi. O programa deve fornecer 5 tentativas ao usuário
# e dizer se o número é maior ou menor a cada tentativa.

import random

n_secreto = random.randint(1, 10)
tentativas = 5
chute = int(input('Digite um número de 0 a 10: '))

while tentativas > 0:
    if chute < n_secreto:
        tentativas -= 1
        chute = int(input(f' Você chutou baixo! Tente novamente. Tentativas: {tentativas} '))
    if chute > n_secreto:
        tentativas -= 1
        chute = int(input(f' Você chutou baixo! Tente novamente. Tentativas: {tentativas} '))
    if tentativas == 0:
        print(f' Você voce esgotou suas tentativas. {tentativas} ')
    else:
        print(f'Parabens! o número secreto era {n_secreto}')
        break
