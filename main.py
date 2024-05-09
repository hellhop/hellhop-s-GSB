import pyautogui
import subprocess
#import os

pyautogui.alert('hello, user <3')
while True:
    ret = 0
    commandline = str(input('~'))  ##ввод комманды
    if commandline == 'testalert':
        print(commandline)
        pyautogui.alert('~ test alert')
        ret = 1

    if commandline == "install autohotkey":
        subprocess.run(["AutoHotkey_1.1.37.02_setup.exe"])
        ret = 1

    if commandline == "quit":
        break

    if ret==0:
        print('~', commandline, ' ', 'is not found')
