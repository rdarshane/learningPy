import time
from win32gui import GetWindowText, GetForegroundWindow

def isActiveWindow(title, sec):

    while (sec >=0):
        handle = GetForegroundWindow()
        winTitle = GetWindowText(handle)
        if title in winTitle:
            return True
        time.sleep(3)
        print(sec)
        sec-=3
    return False

if isActiveWindow("How to Check",10):
    print('window is active')
else:
    print('window not active')

