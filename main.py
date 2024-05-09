import pyautogui
import os
import subprocess
import webbrowser
import fnmatch

def slice(string, start_chars_to_remove, end_chars_to_remove):
    if start_chars_to_remove > len(string) or end_chars_to_remove > len(string):
        return string
    sliced_string = string[start_chars_to_remove:-end_chars_to_remove if end_chars_to_remove > 0 else None]

    return sliced_string

pyautogui.alert('hello, user <3')
ret=int(1)
cstwo=str('steam://rungameid/730')
cssrc=str('steam://rungameid/240')
while True:
    os.chdir('main')
    print(os.listdir())
    dir=str(input('~'))
    os.chdir(dir)
    print(os.listdir())
    if dir=="ahk":
        c = str(input('~'))
        print(len(c))
        ##scriptpath
        text = c
        start_remove = 5 + 1
        end_remove = 0
        result = slice(text, start_remove, end_remove)
        print(result)
        exe = result
        ##appid
        text = c
        start_remove = 0
        end_remove = len(exe) + 1
        result = slice(text, start_remove, end_remove)
        print(result)
        if result == "cssrc":
            webbrowser.open('steam://rungameid/240', new=0, autoraise=False)
        if result == "cstwo":
            webbrowser.open('steam://rungameid/730', new=0, autoraise=False)
        subprocess.run([str(exe)])
        break
    if dir=="quit":
        break











