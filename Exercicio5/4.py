def contar_vogais(palavra):
    vogais = "aeiouAEIOU"
    contador = 0
    for letra in palavra:
        if letra in vogais:
            contador += 1
    return contador

palavra = input("Digite uma palavra para contar as vogais: ")
quantidade_vogais = contar_vogais(palavra)
print(f"A quantidade de vogais na palavra '{palavra}' é: {quantidade_vogais}")
