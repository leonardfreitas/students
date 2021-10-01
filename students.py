import config

qtde_notas = int(input("Quantidade de notas: "))
alunos = []
notas = []

nome = input("Nome do Aluno: ")
alunos.append({"nome": nome, "notas": []})

i = 1
soma = 0
while i <= qtde_notas:
    nota = float(input(f'Nota {i}: '))
    if nota > config.nota_minina and nota < config.nota_maxima:
        notas.append(nota)
        soma = soma + nota
        i += 1
    else:
        print("Erro! Nota inválida")

alunos[0]["notas"] = notas

media = soma / qtde_notas

if media < config.media_global:
    print("Reprovado")
elif media < config.nota_maxima:
    print("Aprovado")
else:
    print("Nota máxima")

print("As notas digitadas foram: ")
for aluno in alunos:
    print(aluno)
