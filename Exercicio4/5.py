numeros = list(map(int, input("Digite os números inteiros, separados por espaço: ").split()))
numero_especifico = int(input("Digite o número a ser contado: "))
ocorrencias = numeros.count(numero_especifico)
print(f"O número {numero_especifico} aparece {ocorrencias} vezes na lista.")
