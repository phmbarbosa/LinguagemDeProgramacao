a = int(input("Digite o primeiro número do intervalo: "))
b = int(input("Digite o segundo número do intervalo: "))

print("Números ímpares no intervalo:")
for i in range(a, b + 1):
    if i % 2 != 0:
        print(i)
