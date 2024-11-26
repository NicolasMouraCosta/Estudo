nicolas = {
    "nome": "Nicolas Moura Costa",
    "idade": 21,
    "CPF": 5035565666 
}

lucas = {
       "nome": "Lucas Thomaz Moura Costa",
    "idade": "18",
    "CPF": "503.679.442-21"
    
}
op = int (input("NICOLAS [1]    |   LUCAS [2] \n"))

if op == 1:
    print("NOME DO CLIENTE:", nicolas['nome'])
    print("IDADE:", nicolas['idade'])
    print("CPF:", nicolas['CPF'])
elif op ==2:
    print("NOME DO CLIENTE:", lucas['nome'])
    print("IDADE:", lucas['idade'])
    print("CPF:", lucas['CPF'])
else:
    print("Opção inválida.")
    