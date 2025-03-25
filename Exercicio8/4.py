def acesso_lista():
    lista = [10, 20, 30, 40, 50]
    
    try:
        indice = int(input("Digite um índice para acessar o valor da lista (0-4): "))
        print(f"O valor no índice {indice} é: {lista[indice]}")
    except IndexError:
        print("Erro: Índice fora do intervalo válido.")
    except ValueError:
        print("Erro: Por favor, digite um número válido como índice.")
        
acesso_lista()
