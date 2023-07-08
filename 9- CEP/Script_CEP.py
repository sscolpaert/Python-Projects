# O script executará uma confirmação do que é um CEP, e o que não é.
import re
CEP = str(input('Entre com o número do CEP, sem ponto mas com hifen: \n'))
if re.search('\d{3}\d{2}-\d{3}', CEP):
    print('Numero CEP validado')
else:
    print('Número do CEP fora do padrão')
input('Pressione Enter para sair...')