numeros = list(map(int, input("Digite os números inteiros, separados por espaço: ").split()))

maior_numero = max(numeros)
menor_numero = min(numeros)

print(f"O maior número da lista é: {maior_numero}")
print(f"O menor número da lista é: {menor_numero}")
