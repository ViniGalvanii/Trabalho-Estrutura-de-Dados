class Venda:
    def __init__(self, id, cliente, produto, quantidade):
        self.id = id
        self.cliente = cliente
        self.produto = produto
        self.quantidade = quantidade
        self.valor_total = quantidade * produto.preco

    def __str__(self):
        return (
            f"Venda ID: {self.id} | Cliente: {self.cliente.nome} | "
            f"Produto: {self.produto.nome} | Qtd: {self.quantidade} | "
            f"Total: R${self.valor_total:.2f}"
        )