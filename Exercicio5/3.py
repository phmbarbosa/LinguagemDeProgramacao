def calcular_media(lista):
    return sum(lista) / len(lista) if lista else 0

numeros = list(map(float, input("Digite os números, separados por espaço: ").split()))
media = calcular_media(numeros)
print(f"A média dos números fornecidos é: {media}")
