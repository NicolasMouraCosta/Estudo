notas_alunos = []

# Coletando informações de 6 alunos
for x in range(2):
    nome_Aluno = input("INFORME SEU NOME\n")
    matricula_Aluno = int(input("INFORME SUA MATRICULA\n"))
    nota = float(input("INFORME A NOTA: "))  # Renomeando 'notas' para 'nota'
    
    # Armazenando nome e nota como uma tupla
    notas_alunos.append((nome_Aluno, nota))

# Exibindo a quantidade de notas registradas
print("QUANTIDADE DE NOTAS:", len(notas_alunos))

# Exibindo os resultados de cada aluno
for n in notas_alunos:
    nome_Aluno = n[0]
   
    print(f'O ALUNO {nome_Aluno} TIROU A NOTA {nota}')
    
    # Verificando a aprovação
    if nota >= 6:
        print('APROVADO')
    else:
        print("REPROVADO")
