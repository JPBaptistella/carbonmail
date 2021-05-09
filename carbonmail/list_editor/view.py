#É onde fica o código para a interface gráfica
#Tudo de existir de Visual vai ficar aqui
#É principalmente aqui que usaremos o PySimpleGUI
import PySimpleGUI as sg
from carbonmail.utils import inner_element_space

lista=['Administradores','Alunos']

def get_layout():

    frame_list = [
        inner_element_space(600),
        [
            sg.Text('Selecione a Lista:'),
            sg.Combo(lista, default_value=lista[1], key='-List-')
        ],
        [
            sg.Text('Criar uma lista'),
            sg.In(key='-ListName-'),
            sg.Button('Criar', key='-Create-', size=(10,1)),
        ],
        [
            sg.Button(
                'Deletar a Lista',
                key='-Delete-',
                size=(15,1),
                pad = (5,(7,7)),
            ),
            sg.Button(
                'Mostrar Contatos',
                key='-Show-',
                size=(15,1),
                pad = (5,(7,7)),
            ),
        ],
        inner_element_space(600),
    ]

    frame_import = [
        inner_element_space(600),
        [
            sg.Text(
                'Selecione o arquivo (CSV):',
                tooltip='Caveçalhos: name e email'
                ),
            sg.In(key='-CSV-'),
            sg.FileBrowse(
                'Selecionar',
                file_types=(('CSV','*.csv'),),
                tooltip='Caveçalhos: name e email',
                ),
        ],
        [
            sg.Button(
                'Importar Contatos',
                key='-Import-',
                size=(15,1),
                pad = (0,(7,7)),
                ),
        ],
        inner_element_space(600),
    ]

    frame_add = [
        inner_element_space(600),
        [
            sg.Text('Insira o nome:'),
            sg.In(key='-Name-'),
        ],
        [
            sg.Text('Insira o E-mail:'),
            sg.In(key='-Email-'),
        ],
        [
            sg.Button(
                'Adicionar Contato',
                key='-Add-',
                size=(15,1),
                pad = (0,(7,7)),
                ),
        ],
        inner_element_space(600),
    ]

    layout = [
        [
            sg.Frame(
                'Configurações da Lista',
                 frame_list,
                 element_justification='c',
                )
        ],
        [
            sg.Frame(
                'Importar Contatos',
                frame_import,
                element_justification='c',
            )
        ],
        [
            sg.Frame(
                'Adicionar Contato',
                frame_add,
                element_justification='c',
            )
        ],
        [
            sg.Button(
                'Voltar',
                key='-Back-',
                size=(15,1),
                pad = (0,(7,7)),
            )
        ],
        inner_element_space(600),
    ]

    return layout

def get_window():
    sg.theme('SandyBeach')
    return sg.Window(
        'Editor de Listas', 
        get_layout(),
        element_justification='c',
        )