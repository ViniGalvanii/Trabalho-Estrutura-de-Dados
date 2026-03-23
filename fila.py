class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def listar(self):
        if not self.itens:
            print("Nenhuma venda registrada.")
            return

        for item in self.itens:
            print(item)

    def calcular_total_vendas(self):
        total = 0

        for venda in self.itens:
            total += venda.valor_total

        return total

    def calcular_gastos_por_cliente(self):
        gastos = {}

        for venda in self.itens:
            nome = venda.cliente.nome

            if nome not in gastos:
                gastos[nome] = 0

            gastos[nome] += venda.valor_total

        return gastos
