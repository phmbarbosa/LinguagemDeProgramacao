class SaldoInsuficienteError(Exception):
    pass

def operacoes_bancarias():
    saldo = 1000.00
    
    try:
        saque = float(input("Digite o valor para saque: R$ "))
        
        if saque > saldo:
            raise SaldoInsuficienteError("Saldo insuficiente para o saque.")
        
        saldo -= saque
        print(f"Saque realizado com sucesso! Novo saldo: R$ {saldo:.2f}")
    
    except SaldoInsuficienteError as e:
        print(f"Erro: {e}")
    except ValueError:
        print("Erro: Digite um valor numérico válido para o saque.")
        
operacoes_bancarias()
