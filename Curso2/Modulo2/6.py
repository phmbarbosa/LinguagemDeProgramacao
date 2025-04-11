try:
    num1 = float(input("Digite o primeiro número: "))
    num2 = float(input("Digite o segundo número: "))

    resultado = num1 / num2
    print(f"\nResultado da divisão: {resultado}")

except ZeroDivisionError:
    print("\nErro: Não é possível dividir por zero.")

except ValueError:
    print("\nErro: Entrada inválida. Por favor, digite números válidos.")

except Exception as e:
    print(f"\nOcorreu um erro inesperado: {e}")
