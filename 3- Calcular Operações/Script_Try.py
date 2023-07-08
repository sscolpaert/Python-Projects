# Calcular Divisão entre 2 números.
try:
    numero1 = float(input('Entre com o primeiro número: '))
    numero2 = float(input('Entre com o segundo número: '))
    resultado = numero1 / numero2
    print("O resultado é: ",resultado)
except ValueError:
    print("Valor inválido!")
except ZeroDivisionError:
    print("Não é possível divisão por zero")
input('Pressione Enter para sair...')