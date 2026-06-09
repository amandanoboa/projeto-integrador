import csv
import sqlite3

conexao = sqlite3.connect("clientes.db")
cursor = conexao.cursor()

cursor.execute("DROP TABLE IF EXISTS clientes")

cursor.execute("""
CREATE TABLE clientes (
    id INTEGER PRIMARY KEY,
    nome TEXT NOT NULL,
    email TEXT NOT NULL
)
""")

with open("clientes.csv", "r", encoding="utf-8") as arquivo:
    leitor = csv.DictReader(arquivo)

    for linha in leitor:
        cursor.execute(
            "INSERT INTO clientes (id, nome, email) VALUES (?, ?, ?)",
            (linha["id"], linha["nome"], linha["email"])
        )

conexao.commit()

cursor.execute("SELECT * FROM clientes")
clientes = cursor.fetchall()

print("Dados importados com sucesso!")
print("Registros inseridos no banco de dados:")

for cliente in clientes:
    print(cliente)

conexao.close()