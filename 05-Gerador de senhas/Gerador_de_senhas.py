import random
import time

print("Aqui vamos criar um gerador de senhas.")
time.sleep(1)
num_caracteres = int(input("Escolha o número de caracteres para a senha:\n1:SIMPLES (4 caracteres somente números)"
                           "\n2:MÉDIO (8 caracteres incluindo caracteres especiais)\n3:FORTE (10 caracteres incluindo caracteres especiais)"
                           "\nESCOLHA: "))
if num_caracteres == 1:
    caracteres = "0123456789"
    tamanho = 4
    senha = "".join(random.sample(caracteres, tamanho))
    print("Senha gerada:", senha)
elif num_caracteres == 2:
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    tamanho = 8
    senha = "".join(random.sample(caracteres, tamanho))
    print("Senha gerada:", senha)
elif num_caracteres == 3:
    caracteres = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()"
    tamanho = 10
    print("Gerando senha forte...")
    time.sleep(2)
    senha = "".join(random.sample(caracteres, tamanho))
    print("Senha gerada:", senha)
else:
    print("Opção inválida. Por favor, escolha 1, 2 ou 3.")
    exit()
