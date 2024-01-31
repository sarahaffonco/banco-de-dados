import sqlite3
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()

#cursor.execute ('CREATE TABLE clientes (id integer PRIMARY KEY AUTO_INCREMENT, nome VARCHAR(100), idade INT, saldo FLOAT)')
#cursor.execute('INSERT INTO clientes (id, nome, idade, saldo) VALUES (5, "Caio", 30, 3000)')
#dados = cursor.execute ('SELECT nome, idade FROM clientes WHERE idade > 30')

#cursor.execute ('SELECT SUM(saldo) / COUNT(*) AS media_saldo FROM clientes')
#media_saldo = cursor.fetchone()[0]
#num_clientes = cursor.rowcount
#print(f"Saldo médio: {media_saldo}")
#dados = cursor.execute ('SELECT * FROM clientes ORDER BY saldo DESC LIMIT 1')
#dados = cursor.execute ('SELECT * FROM clientes WHERE saldo > 1000')
#dados = cursor.execute ( 'UPDATE clientes SET saldo = 5000 WHERE id=2')

dados = cursor.execute ('DELETE FROM clientes where id=3')
for clientes in dados:
     print (clientes)

conexao.commit()

cursor.close()
conexao.close()