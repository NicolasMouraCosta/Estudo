import PySimpleGUI as sg

# Definir tema e layout
sg.theme('Reddit')
layout = [
    [sg.Text('Usuário'), sg.Input(key='usuario')],
    [sg.Text('Senha'), sg.Input(key='senha', password_char='*')],
    [sg.Checkbox('Salvar o login?', key='salvar')],
    [sg.Button('Entrar')]
]

# Criar janela
janela = sg.Window('Tela de login', layout)

# Loop de eventos
while True:
    eventos, valores = janela.read()  # Correção do operador de atribuição
    if eventos == sg.WINDOW_CLOSED:  # Fechar a janela
        break
    if eventos == 'Entrar':
        # Verificar login
        if valores['usuario'] == 'Nicolas' and valores['senha'] == '12345':
            print('BEM VINDO')
        else:
            print('Usuário ou senha incorretos!')

# Fechar janela ao término
janela.close()
