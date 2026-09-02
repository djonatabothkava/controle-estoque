from flask import Flask, render_template, request, redirect
from database import (
    criar_tabela,
    adicionar_produto,
    listar_produtos,
    buscar_produto,
    atualizar_produto,
    excluir_produto
)

app = Flask(__name__)

criar_tabela()

@app.route("/excluir/<int:id>")
def excluir(id):

    excluir_produto(id)

    return redirect("/")


@app.route("/")
def inicio():
    produtos = listar_produtos()

    return render_template("index.html", produtos=produtos)


@app.route("/cadastrar", methods=["POST"])
def cadastrar():

    nome = request.form["nome"]
    categoria = request.form["categoria"]
    quantidade = int(request.form["quantidade"])
    preco = float(request.form["preco"])

    adicionar_produto(nome, categoria, quantidade, preco)

    return redirect("/")

@app.route("/editar/<int:id>")
def editar(id):

    produto = buscar_produto(id)

    if produto is None:
        return "Produto não encontrado", 404 

    return render_template("editar.html", produto=produto)

@app.route("/editar/<int:id>", methods=["POST"])
def salvar_edicao(id):

    nome = request.form["nome"]
    categoria = request.form["categoria"]
    quantidade = int(request.form["quantidade"])
    preco = float(request.form["preco"])

    atualizar_produto(
        id,
        nome,
        categoria,
        quantidade,
        preco
    )

    return redirect("/") 
    

if __name__ == "__main__":
    app.run(debug=True)