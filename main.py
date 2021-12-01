#Importando as páginas do projeto e a biblioteca sqlite3
#from os import startfile
import sqlite3
from time import sleep


#Criando o banco de dados e o seu cursor
banco = sqlite3.connect("Produtos.db")
cursor = banco.cursor()

#Comando usado para criar a tabela do projeto
#cursor.execute("CREATE TABLE IF NOT EXISTS Informacoes (id INTEGER PRIMARY KEY, nome TEXT, preco INTEGER, quantidade INTEGER)")


def telaPrincipal():
    print("-=" * 50)

    print("Cadastrar[1]: ")
    print("Excluir[2]: ")
    print("Alterar[3]: ")
    print("Fechar[4]: ")

    print("-=" * 50)

    #Pergunta a qual será responsável por perguntar o que o usuário quer fazer no momento
    pergunta  = str(input("\nDigite qual operação você quer realizar: ")).strip()

    if pergunta == '1':
        from cadastro import sistemaCadastro
        sistemaCadastro()
            
    elif pergunta == '2':
        from excluir import sistemaExcluir
        sistemaExcluir()
            
    elif pergunta == '3':
        from alterar import sistemaAlterar
        sistemaAlterar()

    elif pergunta == '4':
        quit()

    else:
        print('Operação inválida, tente novamente.')
        telaPrincipal()

    banco.commit()

    cursor.execute('SELECT * FROM Informacoes')

telaPrincipal()

sleep(3)