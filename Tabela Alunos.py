## exercicio banco de dados
import sqlite3
conexao = sqlite3.connect('banco')
cursor = conexao.cursor()


# cursor.execute('CREATE TABLE alunos(id INT, nome VARCHAR(100), idade INT, curso VARCHAR(100))')

# cursor.execute('INSERT INTO alunos(id, nome, idade, curso) VALUES (6, "Joao", 30, "fisica")')


# dados = cursor.execute ('SELECT * FROM alunos')
# for alunos in dados:
#    print (alunos)

# dados = cursor.execute ('SELECT * FROM alunos WHERE curso = "Engenharia" ORDER BY nome')
# for alunos in dados:
#     print (alunos)

# dados = cursor.execute ('SELECT COUNT(*) FROM alunos')
# for alunos in dados:
#    print (alunos)
#conexao.commit()

#dados = cursor.execute ('SELECT * FROM alunos')
#for alunos in dados:
#    print (alunos)
#cursor.execute ( 'UPDATE alunos SET idade = 25 WHERE id=2')
#cursor.execute ('DELETE FROM alunos where id=5')



conexao.commit()

cursor.close()
conexao.close()