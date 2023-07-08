# O script executará uma confirmação do que é um CPF, e o que não é.
import re
CPF = str(input('Entre com o número do CPF, sem ponto e hífen: \n'))
if re.search('\d{11}', CPF):
    print('Número CPF validado')
else:
    print('Número do CPF fora do padrão')
input('Pressione Enter para sair...')