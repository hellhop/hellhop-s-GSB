import pyautogui
pyautogui.alert('hello, user <3')
cycle = 1
while cycle==1:
    commandline = str(input('~'))  ##ввод комманды
    if commandline == 'testalert':
        print(commandline)
        pyautogui.alert('~ test alert')
    else:
        print('~', commandline, ' ', 'is not found')
