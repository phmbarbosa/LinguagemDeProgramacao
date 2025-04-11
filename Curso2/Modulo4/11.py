class Contador:
    def __init__(self, limite):
        self.atual = 1
        self.limite = limite

    def __iter__(self):
        return self

    def __next__(self):
        if self.atual <= self.limite:
            valor = self.atual
            self.atual += 1
            return valor
        else:
            raise StopIteration

n = int(input("Contar até: "))
for i in Contador(n):
    print(i)
