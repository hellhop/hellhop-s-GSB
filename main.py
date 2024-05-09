import pyautogui
import os
import subprocess
import webbrowser

pyautogui.alert('hello, user <3')
while True:
    ret = 1
    commandline = str(input('~'))  ##ввод комманды
    if commandline == "quit":
        break
    if commandline == "listdir":
        print(os.listdir())
        ret = 0
    ##ahk
    if commandline == "ahk":
        os.chdir('ahk')
        arg = str(input('~ahk/'))
        ret = 0
        if arg == "ahkinstall":
            print("~error: can't create process, will be fixed soon")
            ret = 0
        if arg == "return":
            os.chdir('..')
            ret = 0
        if arg == "cs.nulls":
            pyautogui.alert('open console and press F3')
            webbrowser.open('steam://rungameid/730', new=0, autoraise=False)
            subprocess.run(['nullexec V1.exe'])
            os.chdir('..')
            ret = 0

        if ret == 1:
            print('~', arg, ' ', 'is not found, returning')
            os.chdir('..')



    if ret==1:
        print('~',commandline,' ', 'is not found')
