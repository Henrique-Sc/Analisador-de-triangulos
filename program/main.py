# Imports e cores
from functions import dados, format
from time import sleep

reset = '\033[m'
italico = '\033[3m'

# Introdução do programa - o que serve
format.title('Analisador de triângulos', cor=3)

sleep(1)

print(f'''{italico}
Com base no comprimento dos triângulos informados, retorna dados, como: 
    > tipo de triângulo
    > área
    > perímetro
    > ângulos
    > Equivalência entre os triângulos informados {reset}\n''')

sleep(1)

# Quantidades de triângulos que vai analisar
quant_triang = dados.leiaInt('-> Quantos triângulos deseja analisar? ')



# Fazer uma opção para ver uma imagem de exemplo para visualizar as informações

# Inserir dados do triângulo

# Análise do triângulo

# Mostrar na tela o resultado
