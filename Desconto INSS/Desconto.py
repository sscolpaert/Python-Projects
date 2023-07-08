# EXERCÍCIO:
# Crie um script para calcular o desconto do INSS, de acordo com o salário informado pelo usuário, conforme a tabela de desconto abaixo:

# Salário                           Desconto        

# Até R$ 1693,72                    8%      

# De R$ 1693,73 a R$ 2822,90        9%      

# De R$ 2822,91 a R$ 5645,80        11%    

# Acima de R$ 5645,80               O desconto é de R$ 621,04.

print("\n* * * MOSTRA O DESCONTO DO INSS! * * *\n")
salario = float(input('Entre com o salário: '))
if salario <=1693.72:
    inss = float(salario * 0.08)
elif salario >=1693.73 and salario <= 2822.90:
    inss = salario * 0.09
elif salario >=2822.91 and salario <= 5645.80:
    inss = salario * 0.11
else:
    inss = 621.04
print("O desconto do INSS será de: \n","%.2f"% inss)
input('Pressione ENTER para sair...')