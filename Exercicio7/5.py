produtos = {
    101: ("Produto A", 29.99),
    102: ("Produto B", 59.90),
    103: ("Produto C", 19.75)
}

codigo = int(input("Digite o código do produto: "))
if codigo in produtos:
    nome, preco = produtos[codigo]
    print(f"Produto: {nome}, Preço: R$ {preco:.2f}")
else:
    print("Produto não encontrado.")
