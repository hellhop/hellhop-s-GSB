import pyautogui
import os

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
            #ahk launch
            pyautogui.alert('run cs, open console and press F3')
            os.chdir('..')
            ret = 0

        if ret == 1:
            print('~', arg, ' ', 'is not found, returning')
            os.chdir('..')



    if ret==1:
        print('~',commandline,' ', 'is not found')
