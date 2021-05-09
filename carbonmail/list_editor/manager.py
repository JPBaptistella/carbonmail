#Onde estarão todas as funções deste pacote
#Ele quem vai coordenar este pacote (gerenciador)

def initialize(email_sender):
    
    from carbonmail.list_editor import List_Editor #Import dentro do def para importar somente quando eu quiser o email_sender

    ems = List_Editor(email_sender)
    ems.enable_window()