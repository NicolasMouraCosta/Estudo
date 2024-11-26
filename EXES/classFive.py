clientesLN = ['Roby', 'Rony', 'Vitor', 'Kik']  # Usando lista 

print('BEM VINDO A LISTA DE CLIENTES\n')
print('ESTA SÂO A LISTA\n')
print(clientesLN)

# Pergunta se o usuário deseja adicionar um novo nome
print('DESEJA ADD ALGUM\n? ')
op = int (input(" SIM[1] | NÂO[2]"))
if op == 2:
    print('OK TCHAU TCHAU')
else:
    nome = input("INFORME O NOME: ")
    
    
# Adiciona o nome na lista
clientesLN.append(nome)

print('FICOU ASSIM \n')
print(clientesLN)