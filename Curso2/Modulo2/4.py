def contar_vogais(frase):
    vogais = 'aeiou'
    contagem = {vogal: 0 for vogal in vogais}
    for letra in frase.lower():
        if letra in contagem:
            contagem[letra] += 1
    return contagem

frase = input("Digite uma frase: ")

contagem = contar_vogais(frase)
print("\nQuantidade de vogais:")
for vogal, qtd in contagem.items():
    print(f"{vogal}: {qtd}")

print("\nFrase ao contrário:")
print(frase[::-1])

print("\nFrase com espaços substituídos por hífens:")
print(frase.replace(" ", "-"))
