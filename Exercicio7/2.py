palavra = input("Digite uma palavra: ")
contagem = {}
for char in palavra:
    if char in contagem:
        contagem[char] += 1
    else:
        contagem[char] = 1

print(contagem)
