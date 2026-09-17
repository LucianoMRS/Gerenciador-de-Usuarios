import sqlite3

conexao = sqlite3.connect("teste.db")
cursor = conexao.cursor()


cursor.execute("""
CREATE TABLE IF NOT EXISTS usuarios(
                id INTEGER PRIMARY KEY,
                nome TEXT NOT NULL,
                idade REAL NOT NULL,
                email TEXT NOT NULL,
                telefone TEXT DEFAULT 'SEM-TELEFONE'
)""")

conexao.commit()

while True:

    print("\n 1 - adicionar usuários\n\n 2 - mostrar todos (A-Z)\n\n 3 - editar usuario \n\n 4 - remover usuario\n\n 0 - Sair\n")
    escolha = input("\nescolha as opções dado os subcomandos numéricos: ")

    if escolha == "1":
        while True:
            nome = input("\nQual o nome do usuario: ")
            if nome == "":
                break
            idade = int(input("\nQual a idade do usuario: "))
            email = input("\nQual é o email do usuario: ")
            telefone = input("\nQual é o telefone do usuario: ")

            cursor.execute("INSERT INTO usuarios (nome, idade, email, telefone) VALUES (?,?,?,?)", (nome, idade, email, telefone))
            conexao.commit()
        
    elif escolha == "2":
        print("\n 2 - Mostrar todos os usuários\n\n 2.1 - Mostrar todos os usuários cadastrados maiores de idade\n\n 2.2 - Mostrar todos os usuários cadastrados menores de idade\n")
        escolha2 = input("escolha uma das opções dadas acima: \n")
    
        if escolha2 == "2":
            cursor.execute("SELECT id, nome, idade, email, telefone FROM usuarios")
            usuario = cursor.fetchall()

            for n in usuario:
                id, nome, idade, email, telefone = n
                print(f"ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")
           
        elif escolha2 == "2.1":
            cursor.execute("SELECT id, nome, idade, email, telefone FROM usuarios WHERE idade >= 18")
            usuario = cursor.fetchall()

            for n in usuario:
                id, nome, idade, email, telefone = n
                print(f"ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")
            
        elif escolha2 == "2.2":
            cursor.execute("SELECT id, nome, idade, email, telefone FROM usuarios WHERE idade < 18")
            usuario = cursor.fetchall()

            for n in usuario:
                id, nome, idade, email, telefone = n
                print(f"ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")
         

    elif escolha == "3":
        cursor.execute("SELECT id, nome, idade, email, telefone FROM usuarios")
        usuario = cursor.fetchall()
        
        for n in usuario:
            id, nome, idade, email, telefone = n
            print(f"ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")

        id_escolha = int(input("digite o id do usuario que deseja alterar os dados: "))

        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_escolha,))
        usuario = cursor.fetchone()

        if usuario is None:
            print("\nID não encontrado. Tente novamente.\n")
            continue

        print("Esses são os campos que podem ser alterados \n|nome|\n|idade|\n|email|\n|telefone|")
        escolha3 = input("Qual campo deseja alterar: ")

        if escolha3 == "nome":
            nome = input("Digite o novo nome: ")
            cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (nome, id_escolha))
        
            conexao.commit()

        elif escolha3 == "idade":
            idade = int(input("Digite a nova idade: "))
            cursor.execute("UPDATE usuarios SET idade = ? WHERE id = ?", (idade, id_escolha))
            conexao.commit()

        elif escolha3 == "email":
            email = input("Digite o novo email: ")
            cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (email, id_escolha))
            conexao.commit()

        elif escolha3 == "telefone":
            telefone = input("Digite o novo telefone: ")
            cursor.execute("UPDATE usuarios SET telefone = ? WHERE id = ?", (telefone, id_escolha))
            conexao.commit()

        else:
            print("campo não identificado, tente novamente")

    elif escolha == "4":
        cursor.execute("SELECT id, nome, idade, email, telefone FROM usuarios")
        usuario = cursor.fetchall()
        
        for n in usuario:
            id, nome, idade, email, telefone = n
            print(f"ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")

        id_escolha = int(input("digite o id do usuario que deseja remover: "))

        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_escolha,))
        usuario_encontrado = cursor.fetchone()

        if usuario_encontrado is None:
            print("\nID não encontrado. Tente novamente.\n")
            continue

        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_escolha,))
        conexao.commit()

    elif escolha == "0":
        conexao.commit()
        break

    else:
        print("número não identificado com acordo com as opções dadas, tente novamente")