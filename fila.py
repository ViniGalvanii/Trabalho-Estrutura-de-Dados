class Fila:
    def __init__(self):
        self.itens = []

    def enqueue(self, item):
        self.itens.append(item)

    def dequeue(self):
        if self.itens:
            return self.itens.pop(0)
        return None

    def listar(self):
        if not self.itens:
            print("⚠️ Nenhuma venda registrada.")
            return

        for item in self.itens:
            print(item)