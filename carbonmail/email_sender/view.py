#É onde fica o código para a interface gráfica
#Tudo de existir de Visual vai ficar aqui
#É principalmente aqui que usaremos o PySimpleGui

import PySimpleGUI as sg #comando as dá um apelido ao import
from carbonmail.utils import inner_element_space

lista = ['Administradores','Alunos']

def get_layout():

    frame_campaign = [
        inner_element_space(620),
        [
            sg.Text('Selecione o seu Código'),
            sg.In(key='-Code-', size=(30,1)),
            sg.FileBrowse(
                'Selecione',
                file_types=(('Códigos Python','*.py')
                , ),
                size=(15,1),
            ),   
        ],
        [
            sg.Text('Selecione a Lista de Destinatários'),
            sg.Combo(
                lista,
                lista[1],
                key='-Lists-',
                ),
        ],
        inner_element_space(500),
    ]

    frame_email=[
        inner_element_space(500),
        [
            sg.Text(
                'Insira o Titulo',
                ),
        ],
        [
            sg.In(
                key='-Title-',
                size=(62,1),
            ),
        ],
        [
            sg.Text(
                'Insira o Conteúdo do E-mail: ',
                ),
            sg.MLine(
                key='-Content-',
                size=(60,10)
                ),
        ],
        inner_element_space(500),
    ]

    layout = [
        inner_element_space(500),
        [
            sg.Frame(
                'Configurações da Campanha',
                frame_campaign,
                element_justification='c'
                ),
        ],
        [
            sg.Frame(
                'Configurações do E-mail',
                frame_email,
                element_justification='c'
            ),
        ],
        [
            sg.Button(
                'Enviar E-mail',
                key='-Send-',
                size=(15,1),
                pad=(10,(10,0)),
            ),
            sg.Button(
                'Gerenciar Listas',
                key='-ListEditor-', #chama a tela do editor de lista
                size=(15,1),
                pad=(10,(10,0)),
            ),
        ],
        inner_element_space(500),     
    ]
    
    return layout

def get_window():

    sg.theme('SandyBeach')
    return sg.Window(
        'Enviador de E-mail',
         get_layout(),
         element_justification='c',
         )