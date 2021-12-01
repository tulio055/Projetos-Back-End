import sqlite3
from os import error, linesep
from time import sleep

#from alterar import sistemaAlterar

def sistemaCadastro():
    try:
        caminhar = str(input("Deseja continuar operação? CADASTRAR PRODUTO [s/n]\n")).strip().lower()
        caminhar_resposta = caminhar[0]
        if caminhar_resposta == 's':
            try:
                banco = sqlite3.connect('Produtos.db')
                cursor = banco.cursor()

                pergunta_id = int(input("Digite o ID do produto: "))
                pergunta_nome = str(input("Digite o nome do produto: "))
                pergunta_preco = float(input("Digite o preço do produto: "))
                pergunta_quantidade = int(input("Digite a quantidade de produtos: "))

                cursor.execute("INSERT INTO informacoes VALUES ('"+str(pergunta_id)+"', '"+str(pergunta_nome)+"', '"+str(pergunta_preco)+"', '"+str(pergunta_quantidade)+"') ")

                banco.commit()
                print("Os dados foram inseridos com sucesso")

                cursor.execute('SELECT * FROM Informacoes')

                banco.close()

                from main import telaPrincipal
                telaPrincipal()

            except sqlite3.Error as error:
                print(f'Não foi possível executar a ação devido ao erro {error}')
        elif caminhar_resposta == 'n':
            from main import telaPrincipal
            telaPrincipal()

        else:
            print('Valor não reconhecido, tente novamente')
            sistemaCadastro()
    except sqlite3.Error as erro:
        print(f'Não foi possível executar a ação devido ao erro {error}')

sleep(3)