#Onde estarão todas as funções deste pacote
#Ele quem vai coordenar este pacote (gerenciador)

def initialize():
    
    from carbonmail.email_sender import Email_Sender #Import dentro do def para importar somente quando eu quiser o email_sender

    ems = Email_Sender()
    ems.enable_window()
