import pyautogui
import subprocess
#import os

pyautogui.alert('hello, user <3')
while True:
    ret = 0
    commandline = str(input('~'))  ##ввод комманды
    if commandline=="gsb.list":
        print('list is not printable now')
        ret = 1

    if commandline == 'testalert':
        pyautogui.alert('~test alert')
        ret = 1

    if commandline == "sgb.install autohotkey":
        print('~AHK installer is not working, we will fix it soon')
        ##subprocess.run(["AutoHotkey_1.1.37.02_setup.exe"])
        ret = 1

    if commandline == "quit":
        break

    if ret==0:
        print('~',commandline,' ', 'is not found')
