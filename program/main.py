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
    > tipo do triângulo
    > área
    > perímetro
    > ângulos
    > equivalência entre os triângulos {reset}\n''')

sleep(1)

# Quantidades de triângulos que vai analisar
quant_triang = dados.leiaInt('-> Quantos triângulos deseja analisar? ')

if quant_triang <= 0:
    print(f'\nDeseja realmente analisar \"{quant_triang}\" triângulos? isso fará com que o programa não execute a '
          f'análise.')
    quant_triang = int(input('Quantos triângulos deseja analizar? ').strip())

# Fazer uma opção para ver uma imagem de exemplo para visualizar as informações


# Inserir dados do triângulo

# Análise do triângulo

# Mostrar na tela o resultado
