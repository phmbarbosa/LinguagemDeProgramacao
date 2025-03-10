numeros = list(map(int, input("Digite os números inteiros, separados por espaço: ").split()))

numeros_sem_duplicatas = []
for numero in numeros:
    if numero not in numeros_sem_duplicatas:
        numeros_sem_duplicatas.append(numero)

print(f"A lista sem duplicatas é: {numeros_sem_duplicatas}")
