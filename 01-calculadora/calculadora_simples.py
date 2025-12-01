#cauculadora simples

import math

print('Bem vindo a calculadora simples')
n1 = float(input('Digite o primeiro numero: ')).strip()
n2 = float(input('Digite o segundo número: ')).strip()
op = input('Digite a operação (+, - , x, /(para divisão): ').strip().lower()
if op == '+':
    resultado = n1 + n2
elif op == '-':
    resultado =  n1 - n2
elif op == 'x':
    resultado = n1 * n2
elif op == '/':
    resultado = n1 / n2
else:
    resultado = 'Operação inválida'
print(resultado)