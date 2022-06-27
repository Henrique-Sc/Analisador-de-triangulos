# Imports e cores
from functions import dados, format
from time import sleep
from PIL import Image

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
quant_triang = dados.receberTriang('-> Quantos triângulos deseja analisar? ')
# Fazer se o usuário digitar um número menor ou igual 0

# Fazer uma opção para ver uma imagem de exemplo para visualizar as informações
esc = dados.escolha('\nDeseja visualizar uma imagem de exemplo para facilitar a inserção e leitura dos dados? S [Sim] '
                    'ou N [Não]: ')

if esc:
    Image.open("../imagens/triangulo.png")


# Inserir dados do triângulo

# Análise do triângulo

# Mostrar na tela o resultado
