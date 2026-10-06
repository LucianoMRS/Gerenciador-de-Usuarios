### Sistema gerenciador de usuários em Python utilizando o banco de dados SQLite com CRUD completo

O código desenvolve um sistema de gerenciamento de usuários e pedidos utilizando **Python** e o banco de dados **SQLite**.

Os principais métodos utilizados são:

- `sqlite3.connect()`: cria ou abre o banco de dados;
- `conexao.cursor()`: cria um cursor para executar comandos;
- `cursor.execute()`: executa instruções **SQL**;
- `cursor.fetchall()` e `cursor.fetchone()`: consultam os registros;
- `conexao.commit()`: salva as alterações realizadas;
- `conexao.close()`: encerra a conexão com o banco de dados.

O programa também realiza operações **CRUD**, permitindo cadastrar, consultar, atualizar e excluir usuários e pedidos.

Além disso, utiliza funções de validação, estruturas como `while`, `for`, `if` e `else`, tratamento de erros com `try` e `except`, e comandos **SQL** como `CREATE`, `INSERT`, `SELECT`, `UPDATE`, `DELETE` e `JOIN`.

Com esses recursos, o sistema consegue armazenar, organizar e relacionar os dados dos usuários com seus respectivos pedidos.
