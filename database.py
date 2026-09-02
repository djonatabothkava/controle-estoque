import sqlite3


def conectar():
    conexao = sqlite3.connect("estoque.db")
    conexao.row_factory = sqlite3.Row
    return conexao


def criar_tabela():
    conexao = conectar()

    conexao.execute("""
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            categoria TEXT NOT NULL,
            quantidade INTEGER NOT NULL DEFAULT 0,
            preco REAL NOT NULL DEFAULT 0
        )
    """)
def adicionar_produto(nome, categoria, quantidade, preco):
    conexao = conectar()

    conexao.execute("""
        INSERT INTO produtos (nome, categoria, quantidade, preco)
        VALUES (?, ?, ?, ?)
    """, (nome, categoria, quantidade, preco))
    conexao.commit()
    conexao.close()

def listar_produtos():
    conexao = conectar()

    produtos = conexao.execute("""
        SELECT * FROM produtos
        ORDER BY id DESC
    """).fetchall()

    conexao.close()

    return produtos

def buscar_produto(id):
    conexao = conectar()

    produto = conexao.execute("""
        SELECT * FROM produtos
        WHERE id = ?
    """, (id,)).fetchone()

    conexao.close()

    return produto

def atualizar_produto(id, nome, categoria, quantidade, preco):
    conexao = conectar()

    conexao.execute("""
        UPDATE produtos
        SET nome = ?,
            categoria = ?,
            quantidade = ?,
            preco = ?
        WHERE id = ?
    """, (nome, categoria, quantidade, preco, id))

    conexao.commit()
    conexao.close()


def excluir_produto(id):
    conexao = conectar()

    conexao.execute("""
        DELETE FROM produtos
        WHERE id = ?
    """, (id,))

    conexao.commit()
    conexao.close()

def contar_produtos():
    conexao = conectar()

    resultado = conexao.execute("""
        SELECT COUNT(*) AS total
        FROM produtos
    """).fetchone()

    conexao.close()

    return resultado["total"]

def quantidade_total():
    conexao = conectar()

    resultado = conexao.execute("""
        SELECT COALESCE(SUM(quantidade), 0) AS total
        FROM produtos
    """).fetchone()

    conexao.close()

    return resultado["total"]

def valor_total_estoque():
    conexao = conectar()

    resultado = conexao.execute("""
        SELECT COALESCE(SUM(quantidade * preco), 0) AS total
        FROM produtos
    """).fetchone()

    conexao.close()

    return resultado["total"]