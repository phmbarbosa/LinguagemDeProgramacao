frase = input("Digite uma frase: ").split()
contagem_palavras = {}
for palavra in frase:
    if palavra in contagem_palavras:
        contagem_palavras[palavra] += 1
    else:
        contagem_palavras[palavra] = 1

print(contagem_palavras)
