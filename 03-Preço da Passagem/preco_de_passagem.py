# Criar programa que calcule o preço da passagem como 0,50 por km para viagens de até 200km e 0,45 para viagens mais longas.

cidade = ['1 Ji-Paraná', '2 Pimenta Bueno', '3 Cacoal', '4 Vilhena']
print('''Cidades disponíveis: 1 Ji-Paraná, 2 Pimenta Bueno, 3 Cacoal, 4 Vilhena''')
while True:
    destino = int(
        input('Digite algum dos númenos para escolher o seu destino: '))
    if destino >= 1 and destino <= 4:
        break
    print('Número inválido! Tente novamente. ')

print(f'Você escolheu {cidade[destino - 1]} como destino! ')

while True:
    cidade_origem = int(input('Digite o número da cidade de origem: '))
    if cidade_origem >= 1 and cidade_origem <= 4 and cidade_origem != destino:
        break
    print('Você escolheu a mesma cidade de destino! Tente novamente. ')
print(f'Você escolheu {cidade[cidade_origem - 1]} como cidade de origem! ')
print('Calculando o preço da passagem... ')
if (destino == 1 and cidade_origem == 2) or (destino == 2 and cidade_origem == 1):
    distancia = 130
    preco = distancia * 0.50
    print(
        f'A distância entre {cidade[destino - 1]} e {cidade[cidade_origem - 1]} é de {distancia}km. ')
    print(f'O preço da passagem é R$ {preco:.2f} ')
elif (destino == 1 and cidade_origem == 3) or (destino == 3 and cidade_origem == 1):
    distancia = 300
    preco = distancia * 0.45
    print(
        f'A distância entre {cidade[destino - 1]} e {cidade[cidade_origem - 1]} é de {distancia}km. ')
    print(f'O preço da passagem é R$ {preco:.2f} ')
elif (destino == 1 and cidade_origem == 4) or (destino == 4 and cidade_origem == 1):
    distancia = 480
    preco = distancia * 0.45
    print(
        f'A distância entre {cidade[destino - 1]} e {cidade[cidade_origem - 1]} é de {distancia}km. ')
    print(f'O preço da passagem é R$ {preco:.2f} ')
elif (destino == 2 and cidade_origem == 3) or (destino == 3 and cidade_origem == 2):
    distancia = 170
    preco = distancia * 0.50
    print(
        f'A distância entre {cidade[destino - 1]} e {cidade[cidade_origem - 1]} é de {distancia}km. ')
    print(f'O preço da passagem é R$ {preco:.2f} ')
elif (destino == 2 and cidade_origem == 4) or (destino == 4 and cidade_origem == 2):
    distancia = 310
    preco = distancia * 0.45
    print(
        f'A distância entre {cidade[destino - 1]} e {cidade[cidade_origem - 1]} é de {distancia}km. ')
    print(f'O preço da passagem é R$ {preco:.2f} ')
elif (destino == 3 and cidade_origem == 4) or (destino == 4 and cidade_origem == 3):
    distancia = 160
    preco = distancia * 0.50
    print(
        f'A distância entre {cidade[destino - 1]} e {cidade[cidade_origem - 1]} é de {distancia}km. ')
    print(f'O preço da passagem é R$ {preco:.2f} ')

# Adicionei várias condições if...elif para calcular o preço da passagem entre as cidades disponíveis.
