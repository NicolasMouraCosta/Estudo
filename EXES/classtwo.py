def saudacao(nome):
    print(f"Olá, {nome}!")
nome = input("INFOMRE SEU NOME\n")
saudacao(nome) 

def calcular_imc(idade_str, altura_str, peso_int):
    # Tenta converter idade e altura
    try:
        idade = int(idade_str)
        altura = float(altura_str)
    except ValueError:
        return "Erro: Idade ou altura em formato inválido."


print(nome, idade_str)