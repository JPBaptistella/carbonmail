#É onde fica o código para a interface gráfica
#Tudo de existir de Visual vai ficar aqui
#É principalmente aqui que usaremos o PySimpleGui

import PySimpleGUI as sg #comando as dá um apelido ao import

lista = ['Administradores','Alunos']

def get_layout():
    layout = [
        [
            sg.Text('Selecione o seu Código'),
            sg.In(),
            sg.FileBrowse('Selecione', file_types=(('Códigos Python','*.py')
                , )
            ,)            
        ],
        [
            sg.Text('Selecione a lista de Destinatários'),
            sg.Combo(lista, default_value=lista[1],),
        ],
        [
            sg.Text('Insira o Titulo: '),
            sg.In(key='-Title-'), #'-x-' é utilizado para armazenar info para ser usada depois
        ],
        [
            sg.Text('Insira o Conteúdo do E-mail: '),
            sg.MLine(key='-Content-'),
        ],
        [
            sg.Button('Enviar',key='-Send-'),
            sg.Button('Gerenciar Listas', key='-ListEditor-'),
        ],
    ]
    
    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window('Teste de Janela', get_layout())