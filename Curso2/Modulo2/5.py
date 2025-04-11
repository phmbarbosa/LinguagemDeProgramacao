entrada = input("Digite uma lista de palavras separadas por espaço: ")

palavras = entrada.split()

ordenadas = sorted(palavras)
print("\nLista ordenada alfabeticamente:")
print(ordenadas)

print("\nNúmero total de palavras:")
print(len(palavras))

maiusculas = [palavra.upper() for palavra in palavras]
print("\nPalavras em maiúsculas:")
print(maiusculas)
