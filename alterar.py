import sqlite3
from os import error
from time import sleep


def sistemaAlterar():
    try:
        caminhar = str(input("Deseja continuar operação? ALTERAR PRODUTO [s/n]\n")).strip().lower()
        caminhar_resposta = caminhar[0]
        if caminhar_resposta == 's':
            try:
                banco = sqlite3.connect('Produtos.db')
                cursor = banco.cursor()


                id_alterar = input('Digite o ID do produto que você quer alterar: ').strip()

                print("\nnome[1]\npreço[2]\nquantidade[3]")

                pergunta_alterar = str(input('\nO que você deseja alterar na tabela: ')).strip()
                retorno_pergunta_alterar = pergunta_alterar[0]

                if pergunta_alterar == "1":
                    novo_nome = str(input("Digite o novo nome do produto: \n"))
                    nome_atualizado = str(novo_nome)
                    id_alterar = str(id_alterar)
                    cursor.execute("UPDATE informacoes SET nome = '{}' WHERE id = {}".format(nome_atualizado, id_alterar))
                    print("Os dados foram Atualizados com sucesso")
                    
                if pergunta_alterar == "2":
                    novo_preco = float(input("Digite o novo Preço do produto: \n"))
                    preco_atualizado = str(novo_preco)
                    id_alterar = str(id_alterar)
                    cursor.execute("UPDATE Informacoes SET preco = '{}' WHERE  id = {}".format(preco_atualizado, id_alterar))
                    print("Os dados foram Atualizados com sucesso")

                if pergunta_alterar == "3":
                    novo_quantidade = str(input("Digite a nova quantidade de produtos: \n"))
                    quantidade_atualizado = str(novo_quantidade)
                    id_alterar = str(id_alterar)
                    cursor.execute("UPDATE Informacoes SET preco = '{}' WHERE  id = {}".format(quantidade_atualizado, id_alterar))
                    print("Os dados foram Atualizados com sucesso")

                elif pergunta_alterar != "1" and pergunta_alterar != "2" and pergunta_alterar != "3":
                    print('Valor não aceitável pelo programa, tente novamente.')
                    sistemaAlterar()

                banco.commit()

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
            sistemaAlterar()

    except sqlite3.Error as error:
                print(f'Não foi possível executar a ação devido ao erro {error}')

sleep(3)