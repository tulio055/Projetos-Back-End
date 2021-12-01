from os import error
import sqlite3
from time import sleep

def sistemaExcluir():
    try:
        caminhar = str(input("Deseja continuar operação? EXCLUIR PRODUTO [s/n]\n")).strip().lower()
        caminhar_resposta = caminhar[0]
        if caminhar_resposta == 's':
            try:
                banco = sqlite3.connect('Produtos.db')
                cursor = banco.cursor()

                pergunta_id = input('Digite o número desejado do ID do produto a ser excluído: ')
                cursor.execute("DELETE FROM Informacoes WHERE id = '"+str(pergunta_id)+"'")

                banco.commit()
                print("Os dados foram removidos com sucesso")

                cursor.execute('SELECT * FROM Informacoes')

                banco.close()

                from main import telaPrincipal
                telaPrincipal()

            except sqlite3.Error as error :
                print(f'Não foi possível executar a ação devido ao erro {error}')

        elif caminhar_resposta == 'n':
            from main import telaPrincipal
            telaPrincipal()
        
        else:
            print('Valor não reconhecido, tente novamente')
            sistemaExcluir()

    except sqlite3.Error as error :
                print(f'Não foi possível executar a ação devido ao erro {error}')

sleep(3)