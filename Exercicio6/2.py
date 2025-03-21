numeros = tuple(int(input(f"Digite o {i+1}º número: ")) for i in range(4))

print(f"Tupla: {numeros}")
print(f"O número 9 apareceu {numeros.count(9)} vezes.")

if 3 in numeros:
    print(f"O primeiro número 3 apareceu na posição {numeros.index(3)}.")
else:
    print("O número 3 não foi digitado.")

pares = [num for num in numeros if num % 2 == 0]
print(f"Números pares: {pares}")
