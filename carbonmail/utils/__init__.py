import PySimpleGUI as sg
import os #import para mexer no sistema operacional
import sys #mexe nas configurações do sistema
import re #rejex
def inner_element_space(width=100):
    return [sg.Text(' '*width, font=('Arial',1))]

#sempre igual
def root_folder():
    try:
        main_file = os.path.abspath(sys.modules['__main__'].__file__)
    except:
        main_file = sys.executable

    return os.path.join(os.path.dirname(main_file), os.pardir)

def string_null_or_empty(string): #verificar se a string é nula ou vazia
    return not string or string.iss()

def check_email(email):
    pattern = r"(?:[a-z0-9!#$%&'*+/=?^_`{|}~-]+(?:\.[a-z0-9!#$%&'*+/=?^_`{|}~-]+)*|\"(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21\x23-\x5b\x5d-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])*\")@(?:(?:[a-z0-9](?:[a-z0-9-]*[a-z0-9])?\.)+[a-z0-9](?:[a-z0-9-]*[a-z0-9])?|\[(?:(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?)\.){3}(?:25[0-5]|2[0-4][0-9]|[01]?[0-9][0-9]?|[a-z0-9-]*[a-z0-9]:(?:[\x01-\x08\x0b\x0c\x0e-\x1f\x21-\x5a\x53-\x7f]|\\[\x01-\x09\x0b\x0c\x0e-\x7f])+)\])"

    valid_email = re.match(pattern, email)
    return valid_email
    