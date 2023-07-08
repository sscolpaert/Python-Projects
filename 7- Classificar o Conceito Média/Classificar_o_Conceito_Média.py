# Ao entrar com a média do aluno, classifica o conceito
media = float(input('Entre com a média do aluno: '))
if media <=5:
    conceito = str("Regular")
elif media < 7:
    conceito = "Bom"
else:
    conceito = "Excelente"
print("Conceito: ",conceito)