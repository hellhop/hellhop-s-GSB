import pyautogui
import os
import subprocess
import webbrowser
import fnmatch

pyautogui.alert('hello, user <3')
ret=int(1)
cs=str('steam://rungameid/730')
while True:
    print('~avaiable dirs:', os.listdir('main'))
    dir=str(input('~'))
    ret=int(1)
    if dir==True:
        os.chdir(dir)
        print('~avaiable dirs:', os.listdir(dir))
        dir_a = str(input('~',dir,'/'))
        if dir_a==True:
            if fnmatch(dir_a, 'cs.*.*'):
                webbrowser.open(cs)



    ##if ret==int(1):
        ##print("~err: not found")
        ##os.chdir('')
        ##ret = int(1)

