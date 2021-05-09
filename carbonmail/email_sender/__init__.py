import PySimpleGUI as sg
from PySimpleGUI import WIN_CLOSED
from carbonmail.email_sender import view
from carbonmail.list_editor.manager import initialize as init_list_editor

class Email_Sender():
    def __init__(self):
        self.window = None

    def instantiate(self): #cria a janela
        if self.window == None:
            self.window = view.get_window()

    def enable_window(self): #habilita e trabalha
        self.instantiate()

        while True:
            event, values = self.window.read()

            if event == WIN_CLOSED:
                self.close_window()
                break

            if event == '-Send-':
                title=values['-Title-']
                content=values['-Content-']

                sg.Popup(
                    f'O Titilo é: {title}\nO Conteúdo é: {content}', #\n configura quebra de linha
                    title='E-mail',
                )

            if event == '-ListEditor-':
                self.hide_window()
                init_list_editor(self)

    def close_window(self): #fecha a janela
        if self.window is not None:
            self.window.Close()
        self.window=None #convenção

    def hide_window(self): #esconde a janela
        if self.window is not None:
            self.window.Hide()

    def unhide_window(self): #mostra a janela
        if self.window is not None:
            self.window.UnHide()
        