from PIL import Image
from time import sleep
from functions import format, dados, analisarTriang

while True:
    try:
        # Resumo sobre o programa
        format.title('Analizador de triângulos', cor=3)
        sleep(1.5)

        print(f'''
{format.formatacao[2]}Com base nas medidas dos lados do triângulo, retorna dados como: 
    > Tipo de triângulo;
    > Área;
    > Perímetro;
    > Ângulos;
    > Altura.{format.formatacao[0]}''')
        sleep(1.5)

        # Perguntar ao usuário quantos triângulos ele quer analizar
        while True:
            quant_Triangs = dados.leiaInt('\nQuantos triângulos deseja analizar? ')
            if quant_Triangs <= 0:
                dados.erro('Digite um valor maior ou igual a 1.')
            else:
                break

        # Linha amarela
        format.flinha(cor=5, simb='-', time=1.5)

        # Fazer uma opção para ver uma imagem de exemplo para visualizar as informações
        print(f'Deseja visualizar uma {format.formatacao[6]}imagem de exemplo{format.formatacao[0]} para facilitar a inserção e leitura dos dados?\n')
        sleep(1.5)
        if dados.escolha():
            try:
                Image.open('images/triangulo.png').show()
            except FileNotFoundError:
                print(dados.erro('Imagem não localizada'))

        # Linha amarela
        format.flinha(cor=5, simb='-', time=0, quebra=False)

        # Inserir os ddos do(s) triângulo(s)
        dados_Triangs = dados.dadosTriang(quant_Triangs)

        # Análise dos dados
        print()
        format.title('Calculando...', cor=5)
        sleep(2)
        print()
        analisarTriang.analise(dados_triangs=dados_Triangs)

        sleep(1.5)

        print('\nFim da execução. Volte sempre (•◡•)/')

        break

    except KeyboardInterrupt:
        print('')
        dados.userInterrupt()
        sleep(1)
        print('')
        format.title('O programa será reiniciado...', 5)
        sleep(2)
        print('')
