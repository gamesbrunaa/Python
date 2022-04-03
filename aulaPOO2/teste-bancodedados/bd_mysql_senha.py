import mysql.connector as mysql

conexao = mysql.connect(host = 'localhost', db = 'pooII', user = 'root', passwd = 'mikasa')
cursor = conexao.cursor()

sql = """CREATE TABLE IF NOT EXISTS usuarios_senha (id integer AUTO_INCREMENT PRIMARY KEY, nome text NOT NULL, senha VARCHAR(32) NOT NULL, email text NOT NULL);"""

nome = 'bruna'
senha = 'teste'
email = 'gamessbrunaa@gmail.com'

cursor.execute(sql)
for x in range(5):
    cursor.execute('INSERT INTO usuarios_senha (nome, senha, email) VALUES (%s, MD5(%s), %s)', (nome, senha, email))

cursor.execute('SELECT * FROM usuarios_senha WHERE nome = %s AND senha = MD5(%s)', (nome, senha))

for c in cursor:
    print(c)