import sqlite3
from datetime import datetime

def conectar_banco():
    conn = sqlite3.connect("historico_imc.db")
    cursor = conn.cursor()
    cursor.execute("""
            CREATE TABLE IF NOT EXISTS historico(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT,
            massa REAL,
            altura REAL,
            imc REAL,
            classificacao TEXT,
            data TEXT
            )  
        """)
    conn.commit()
    return conn, cursor

def salvar_historico(conn, cursor, nome, massa, altura, imc, classificacao):
    data = datetime.now().strftime("%d/%m/%Y %H:%M")
    cursor.execute("""
        INSERT INTO historico (nome, massa, altura, imc, classificacao, data)
        VALUES (?, ?, ?, ?, ?, ?)
        """, (nome, massa, altura, imc, classificacao, data))
    conn.commit()
    
def calcular_imc(massa, altura):
    return massa / (altura ** 2)

def classificar_imc(imc):
    if imc < 17:
        return "Muito abaixo do peso."
    elif imc < 18.5:
        return "Abaixo do peso."
    elif imc < 25:
        return "Peso ideal."
    elif imc < 30:
        return "Sobrepeso."
    elif imc < 35:
        return "Obesidade."
    elif imc < 40:
        return "Obesidade Severa."
    else:
        return "Obesidade Mórbida."

def ver_historico(cursor):
    cursor.execute("SELECT nome, massa, altura, imc, classificacao, data FROM historico")
    registros = cursor.fetchall()

    if not registros:
        print("Nenhum registro encontrado.")
        return

    print("\n=== Histórico ===")
    for r in registros:
        print(f"{r[5]} - {r[0]} | IMC: {r[3]:.2f} | {r[4]}")
def main():
    conn, cursor = conectar_banco()
    nome = input("Digite seu nome: ")
    massa = float(input("Massa (Kg): "))
    altura = float(input("Altura (M): "))
    if massa <= 0 or altura <= 0:
        print("Erro: massa e altura precisam ser maiores que zero.")
        return

    imc = calcular_imc(massa, altura)
    classificacao = classificar_imc(imc)

    print(f"IMC: {imc:.2f}")
    print(f"Classificação: {classificacao}")

    ver_historico(cursor)

    salvar_historico(conn, cursor, nome, massa, altura, imc, classificacao)
    print("Registro salvo!")
main()
