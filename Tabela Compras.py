import sqlite3
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

##cursor.execute ('CREATE TABLE compras (id INTEGER PRIMARY KEY AUTOINCREMENT, cliente_id INT NOT NULL, produto VARCHAR(150) NOT NULL, valor FLOAT NOT NULL, FOREIGN KEY (cliente_id) REFERENCES clientes (id))')
#dados = cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (1, "Caderno", 20.00)')
# dados = cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (2, "Livro", 50.00)')
#dados = cursor.execute ('INSERT INTO compras (cliente_id, produto, valor) VALUES (3, "Caneta", 10.00)')


dados = cursor.execute ('SELECT * FROM compras WHERE cliente_id = 1')
for compras in dados:
    print (compras)
conexao.commit()

cursor.close()
conexao.close()