import psycopg2
import time

# Aguarda o banco
print("Esperando o banco de dados iniciar...")
time.sleep(10)

connection = psycopg2.connect(
    host='db',
    database='meu_db',
    user='postgres',
    password='root',
    port=5432
)

cursor = connection.cursor()

# Cria tabela clientes
cursor.execute("CREATE TABLE IF NOT EXISTS clientes (id SERIAL PRIMARY KEY, nome VARCHAR(255))")

# Insere dois registros
cursor.execute("INSERT INTO clientes (nome) VALUES ('João')")
cursor.execute("INSERT INTO clientes (nome) VALUES ('Maria')")

connection.commit()

# Verifica registros com select básico
cursor.execute("SELECT * FROM clientes")
print("Registros na tabela clientes:")
print(cursor.fetchall())

cursor.close()
connection.close()

print("Tabela criada e dados inseridos com sucesso!")
