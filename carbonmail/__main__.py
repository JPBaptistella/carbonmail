#Arquivo inicial a ser executado
#Quando iniciamos o projeto ele é o primeiro a ser executado
#Ponto de entrada da aplicação

from carbonmail.email_sender.manager import initialize as init_sender
from carbonmail.database.initializer import initialize as init_db

init_db()
init_sender()

