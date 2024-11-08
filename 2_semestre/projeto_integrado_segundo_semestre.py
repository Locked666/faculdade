
from datetime import datetime

# Estrutura para representar um Produto

global inventario , categorias, movimentacoes

class Produto:
    def __init__(self, nome, categoria, quantidade, preco, localizacao):
        self.nome = nome
        self.categoria = categoria
        self.quantidade = quantidade
        self.preco = preco
        self.localizacao = localizacao

# Estrutura para representar uma Categoria
class Categoria:
    def __init__(self, nome):
        self.nome = nome
        self.produtos = []  # Lista de produtos pertencentes à categoria

# Estrutura para representar uma Movimentação de Estoque
class Movimentacao:
    def __init__(self, produto, tipo, quantidade, data):
        self.produto = produto
        self.tipo = tipo  # 'entrada' ou 'saída'
        self.quantidade = quantidade
        self.data = data

# Cadastro de novo produto
def cadastrar_produto(nome, categoria, quantidade, preco, localizacao):
    produto = Produto(nome, categoria, quantidade, preco, localizacao)
    # Adicionar o produto à lista ou banco de dados
    inventario.append(produto)
    print(f"Produto '{nome}' cadastrado com sucesso!")

# Cadastro de nova categoria
def cadastrar_categoria(nome):
    categoria = Categoria(nome)
    categorias.append(categoria)
    print(f"Categoria '{nome}' cadastrada com sucesso!")

# Consulta de um produto específico
def consultar_produto(nome):
    for produto in inventario:
        if produto.nome == nome:
            print(f"Nome: {produto.nome}, Categoria: {produto.categoria}, Quantidade: {produto.quantidade}, Preço: {produto.preco}, Localização: {produto.localizacao}")
            return produto
    print("Produto não encontrado.")
    return None

# Função para registrar a entrada de produtos no estoque
def registrar_entrada(produto_nome, quantidade):
    produto = consultar_produto(produto_nome)
    if produto:
        produto.quantidade += quantidade
        movimentacao = Movimentacao(produto.nome, 'entrada', quantidade, datetime.now())
        movimentacoes.append(movimentacao)
        print(f"Entrada de {quantidade} unidades de '{produto_nome}' registrada.")

# Função para registrar a saída de produtos do estoque
def registrar_saida(produto_nome, quantidade):
    produto = consultar_produto(produto_nome)
    if produto and produto.quantidade >= quantidade:
        produto.quantidade -= quantidade
        movimentacao = Movimentacao(produto.nome, 'saída', quantidade, datetime.now())
        movimentacoes.append(movimentacao)
        print(f"Saída de {quantidade} unidades de '{produto_nome}' registrada.")
    else:
        print("Quantidade insuficiente para saída.")

# Relatório de estoque baixo
def gerar_relatorio_estoque_baixo(limite=10):
    print("Relatório de Produtos com Estoque Baixo:")
    for produto in inventario:
        if produto.quantidade <= limite:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")

# Relatório de excesso de estoque
def gerar_relatorio_excesso_estoque(limite=100):
    print("Relatório de Produtos com Excesso de Estoque:")
    for produto in inventario:
        if produto.quantidade >= limite:
            print(f"Produto: {produto.nome}, Quantidade: {produto.quantidade}")

# Histórico de movimentações
def consultar_historico_movimentacoes():
    print("Histórico de Movimentações:")
    for movimentacao in movimentacoes:
        print(f"Produto: {movimentacao.produto}, Tipo: {movimentacao.tipo}, Quantidade: {movimentacao.quantidade}, Data: {movimentacao.data}")
