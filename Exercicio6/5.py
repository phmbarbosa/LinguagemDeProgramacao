times = ('Flamengo', 'Palmeiras', 'Atlético-MG', 'São Paulo', 'Internacional', 
         'Grêmio', 'Fluminense', 'Santos', 'Corinthians', 'Athletico-PR')

print("Os três primeiros colocados são:")
print(times[:3])

print("Os últimos três colocados são:")
print(times[-3:])

print("Times em ordem alfabética:")
print(sorted(times))

time_busca = input("Digite o nome de um time para saber sua posição: ")

if time_busca in times:
    print(f"O time {time_busca} está na posição {times.index(time_busca) + 1}.")
else:
    print("Time não encontrado.")
