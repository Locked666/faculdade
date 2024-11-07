class Produto:
    def __init__(self, id, nome, categoria,localizacao, quantidade):
        self.id = id
        self.nome = nome
        self.categoria = categoria
        self.localizacao = localizacao
        self.quantidade = quantidade

         
class Categoria:
    def __init__(self, id, nome):
        self.id = id
        self.nome = nome

class Movimentacao:
    def __init__(self, id, produto_id, tipo, quantidade, data):
        self.id = id
        self.produto_id = produto_id
        self.tipo = tipo  # 'entrada' ou 'saida'
        self.quantidade = quantidade
        self.data = data

class SistemaGerenciamentoEstoque:
    def __init__(self):
        self.produtos = []
        self.categorias = []
        self.movimentacoes = []

    def cadastrar_produto(self, produto):
        self.produtos.append(produto)

    def consultar_produto(self, id):
        for produto in self.produtos:
            if produto.id == id:
                return produto
        return None

    def cadastrar_categoria(self, categoria):
        self.categorias.append(categoria)

    def consultar_categoria(self, id):
        for categoria in self.categorias:
            if categoria.id == id:
                return categoria
        return None

    def registrar_movimentacao(self, movimentacao):
        produto = self.consultar_produto(movimentacao.produto_id)
        if produto:
            if movimentacao.tipo == 'entrada':
                produto.quantidade += movimentacao.quantidade
            elif movimentacao.tipo == 'saida' and produto.quantidade >= movimentacao.quantidade:
                produto.quantidade -= movimentacao.quantidade
            self.movimentacoes.append(movimentacao)
        else:
            print("Produto não encontrado.")


    # def registrar_movimentacao(self, movimentacao):
    #     produto = self.consultar_produto(movimentacao.produto_id)
    #     if produto:
    #         if movimentacao.tipo == 'entrada':
    #             produto.quantidade += movimentacao.quantidade
    #         elif movimentacao.tipo == 'saida' and produto.quantidade >= movimentacao.quantidade:
    #             produto.quantidade -= movimentacao.quantidade
    #         self.movimentacoes.append(movimentacao)
    #     else:
    #         print("Produto não encontrado.")

    def gerar_relatorio(self):
        relatorio = []
        for produto in self.produtos:
            relatorio.append({
                'id': produto.id,
                'nome': produto.nome,
                'quantidade': produto.quantidade
            })
        return relatorio

    def consultar_historico_movimentacoes(self, produto_id):
        historico = []
        for movimentacao in self.movimentacoes:
            if movimentacao.produto_id == produto_id:
                historico.append(movimentacao)
        return historico
