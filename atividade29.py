# Crie um programa que receba uma lista com os nomes dos alunos presentes em uma aula e exiba quantos alunos estão presentes e a lista dos nomes. Se o total de alunos presentes for menor que 5, exiba uma mensagem sugerindo uma revisão da lista de chamada.

# Exemplo de entrada:
# Alunos presentes: ['Ana', 'Bruno', 'Carlos', 'Daniela']

# Exemplo de saída:
# Alunos presentes: 4
# Lista de alunos presentes: Ana, Bruno, Carlos, Daniela
# Aviso: Poucos alunos presentes. Revisar lista de chamada.
alunos = []

while True:
    a_presentes = str(input("digite o nome dos alunos presentes (0 para terminar!):  "))
    if a_presentes == "0":
        break
    alunos.append(a_presentes)

alunos_presentes = len(alunos)
print("alunos presentes: ", alunos_presentes)
print(alunos)

if alunos_presentes < 5:
    print("Aviso: a quantidade de alunos presentes é inferior a 5. Considere revisar a lista de chamadas!")