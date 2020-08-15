from tkinter import *
from tkinter.messagebox import showinfo, showerror
from pyautogui import prompt
from os import chdir, mkdir, system, getcwd, listdir
from getpass import getuser

def check_if_default_file_exist():

    print("oi vitor")
    current_path = getcwd()

    content = listdir()
    
    if ".default.txt" not in content:
        response = showinfo(title=".default.txt",message="The file \".default.txt\" does't exit")
        
        while True:

            try:
                file_path = prompt(text="Write the default directory",title="default work directory")
                listdir(file_path)
                chdir(file_path)
                break
            except:
                showerror(title="Error The path {file_path} does't !!")
    
        arquivo = open(".default.txt", "w")
        arquivo.writelines(file_path)
        arquivo.close()

        chdir(file_path)
        print("hey")

        system("pwd")

def write_changes(content, file):
    pass

check_if_default_file_exist()

