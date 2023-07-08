# Criação de um Sistema de sorteio.
import random
print("\n* * * Sorteando três números diferentes entre 1 e 50 * * *\n")
input("Pressione Enter para gerar os números: ")
while True:
    num1 = random.randint(1,50)
    num2 = random.randint(1,50)
    num3 = random.randint(1,50)
    if num1 not in (num2,num3) and num2 != num3:
        break
print("Os números são:\n ", num1, num2, num3)
input("Pressione Enter para sair...")
