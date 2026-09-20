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

cursor.execute("""
CREATE TABLE IF NOT EXISTS pedidos(
                id integer primary key,
                descricao TEXT  NOT NULL,
                valor REAL NOT NULL,
                usuario_id INTEGER,
                FOREIGN KEY (usuario_id) REFERENCES usuarios (id)
)
""")

conexao.commit()

while True:

    escolha = int(input("""===========================================
 1 - adicionar usuários\n 2 - mostrar todos (A-Z)\n 3 - editar usuario
 4 - remover usuario\n 5 - adicionar pedido\n 6 - mostrar usuários com seus pedidos
 7 - exibir pedidos de um usuário específico\n 8 - remover pedido\n 9 - Sair
 ===========================================
 Escolha uma das opções dadas acima: """))
    print(" ===========================================")

#======================================================================================================================================
  
    if escolha == 1:
        while True:
            nome = input("\n Qual o nome do usuario: ")
            if nome == "":
                break
            idade = int(input("\n Qual a idade do usuario: "))
            email = input("\n Qual é o email do usuario: ")
            telefone = input("\n Qual é o telefone do usuario: ")
            print(" ===========================================")

            cursor.execute("INSERT INTO usuarios (nome, idade, email, telefone) VALUES (?,?,?,?)", (nome, idade, email, telefone))
            conexao.commit()
            print(" Usuário adicionado com sucesso!\n")

#======================================================================================================================================       
  
    elif escolha == 2:
        print("\n 2 - Mostrar todos os usuários\n 2.1 - Mostrar todos os usuários cadastrados maiores de idade\n 2.2 - Mostrar todos os usuários cadastrados menores de idade\n")
        escolha2 = input("\n escolha uma das opções dadas acima: ")
    
        if escolha2 == "2":
            cursor.execute("SELECT * FROM usuarios")
            usuario = cursor.fetchall()

            for n in usuario:
                id, nome, idade, email, telefone = n
                print(f"\n ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")
           
        elif escolha2 == "2.1":
            cursor.execute("SELECT * FROM usuarios WHERE idade >= 18")
            usuario = cursor.fetchall()

            for n in usuario:
                id, nome, idade, email, telefone = n
                print(f"\n ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")
            
        elif escolha2 == "2.2":
            cursor.execute("SELECT *FROM usuarios WHERE idade < 18")
            usuario = cursor.fetchall()

            for n in usuario:
                id, nome, idade, email, telefone = n
                print(f"\n ID: {id}\n Nome: {nome}\n Idade: {idade}\n Email: {email}\n Telefone: {telefone}\n")

#======================================================================================================================================
   
    elif escolha == 3:
        cursor.execute("SELECT id, nome FROM usuarios")
        usuario3 = cursor.fetchall()
        
        for n in usuario3:
            id, nome = n
            print(f"\n ID: {id}\n Nome: {nome}\n")

        id_escolha = int(input("\ndigite o id do usuario que deseja alterar os dados: "))

        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_escolha,))
        usuario3 = cursor.fetchone()

        if usuario3 is None:
            print("\n ID não encontrado. Tente novamente.\n")
            continue

        print("\nEsses são os campos que podem ser alterados \n|nome|\n|idade|\n|email|\n|telefone|")
        escolha3 = input(" Qual campo deseja alterar: ")

        if escolha3 == "nome":
            nome = input("\n Digite o novo nome: ")
            cursor.execute("UPDATE usuarios SET nome = ? WHERE id = ?", (nome, id_escolha))
            conexao.commit()
            print("\n Nome alterado com sucesso!\n")

        elif escolha3 == "idade":
            idade = int(input("\n Digite a nova idade: "))
            cursor.execute("UPDATE usuarios SET idade = ? WHERE id = ?", (idade, id_escolha))
            conexao.commit()
            print("\n Idade alterada com sucesso!\n")

        elif escolha3 == "email":
            email = input("\nDigite o novo email: ")
            cursor.execute("UPDATE usuarios SET email = ? WHERE id = ?", (email, id_escolha))
            conexao.commit()
            print("\n Email alterado com sucesso!\n")

        elif escolha3 == "telefone":
            telefone = input("\n Digite o novo telefone: ")
            cursor.execute("UPDATE usuarios SET telefone = ? WHERE id = ?", (telefone, id_escolha))
            conexao.commit()
            print("\n Telefone alterado com sucesso!\n")

        else:
            print("\n campo não identificado, tente novamente")

#======================================================================================================================================
   
    elif escolha == 4:
        cursor.execute("SELECT id, nome FROM usuarios")
        usuario4 = cursor.fetchall()
        
        for n in usuario4:
            id, nome = n
            print(f"\n ID: {id}\n Nome: {nome}\n")

        id_escolha = int(input("\n digite o id do usuario que deseja remover: "))

        cursor.execute("SELECT * FROM usuarios WHERE id = ?", (id_escolha,))
        usuario_encontrado = cursor.fetchone()

        cursor.execute("DELETE FROM pedidos WHERE usuario_id = ?", (id_escolha,))
        cursor.execute("DELETE FROM usuarios WHERE id = ?", (id_escolha,))
        conexao.commit()
        print("\n Usuário removido com sucesso!\n")
        
#======================================================================================================================================
 
    elif escolha == 5:
        cursor.execute("SELECT id, nome FROM usuarios")
        usuario5 = cursor.fetchall()

        for n in usuario5:
            id, nome = n
            print(f"\n ID: {id}\n Nome: {nome}")

        descricao = input("\n Digite a descrição do produto: ")
        valor = float(input("\n Digite o valor do produto: "))
        id_usuario = int(input("\n Digite o ID de um usuário existente para adicionar um pedido: "))
        if id_usuario is None:
         print("\n ID não encontrado. Tente novamente.\n")
         print(" ===========================================")
         break

        cursor.execute("INSERT INTO pedidos (descricao, valor, usuario_id) VALUES (?, ?, ?)", (descricao, valor, id_usuario))
        conexao.commit()
        print("\n Pedido adicionado com sucesso!\n")

#======================================================================================================================================

    elif escolha == 6:
        cursor.execute("""
                        SELECT usuarios.id, usuarios.nome, pedidos.id, pedidos.descricao AS produto, pedidos.valor FROM usuarios
                        JOIN pedidos
                        ON pedidos.usuario_id = usuarios.id
""")
        pedidos = cursor.fetchall()

        for n in pedidos:
            usuario_id, nome, id_pedido, descricao, valor = n
            print(f"\n ID do usuário: {usuario_id}\n Nome: {nome}\n ID do pedido: {id_pedido}\n Produto: {descricao}\n Valor: R${valor:.2f}\n")

#======================================================================================================================================

    elif escolha == 7:
        cursor.execute("SELECT id, nome FROM usuarios")
        usuario7 = cursor.fetchall()

        for n in usuario7:
            id, nome = n
            print(f"\n ID: {id}\n Nome: {nome}\n")

        id_usuario = int(input("\n Digite o ID de um usuário existente para exibir seus pedidos: "))

        if id_usuario is None:
                 print("\n ID não encontrado. Tente novamente.\n")
                 print(" ===========================================")
                 break

        cursor.execute("""
                        SELECT usuarios.nome, pedidos.descricao AS produtos, pedidos.valor FROM pedidos
                        JOIN usuarios
                        ON pedidos.usuario_id = usuarios.id
                        WHERE usuario.id = ?""", (id_usuario,))
        usuario7 = cursor.fetchall()

        for n in usuario7:
            nome, descricao, valor = n
            print(f"\n Pedidos do(a): {nome}\n {descricao} - R${valor:.2f}\n")

#======================================================================================================================================

    elif escolha == 8:
        cursor.execute("SELECT * FROM pedidos")
        usuario8 = cursor.fetchall()

        for n in usuario8:
            id, descricao, valor, usuario_id = n
            print(f"\n  ID: {id}\n Produto: {descricao}\n Valor: R${valor:.2f}\n ID do usuário: {usuario_id}\n")

        escolha8 = int(input("\n Digite o ID do pedido que deseja remover: "))

        cursor.execute("DELETE FROM pedidos WHERE id = ?", (escolha8,))
        conexao.commit()
        print("\n Pedido removido com sucesso!\n")

#======================================================================================================================================

    elif escolha == 9:
        break

#======================================================================================================================================

    else:
        print("\n Número não identificado com acordo com as opções dadas, tente novamente")