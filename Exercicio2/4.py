nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media_aluno = (nota1 + nota2) / 2

if media_aluno >= 7:
    print("Aprovado.")
elif 5 <= media_aluno < 7:
    print("Recuperação.")
else:
    print("Reprovado.")
