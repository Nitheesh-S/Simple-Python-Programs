# http://timgolden.me.uk/pywin32-docs/win32api__GetCursorPos_meth.html
# http://timgolden.me.uk/pywin32-docs/win32api__WinExec_meth.html
# http://timgolden.me.uk/pywin32-docs/win32gui__GetActiveWindow_meth.html
# http://timgolden.me.uk/pywin32-docs/win32gui__GetDesktopWindow_meth.html
# http://timgolden.me.uk/pywin32-docs/win32gui__GetFocus_meth.html
# print(GetWindowText(GetForegroundWindow()))
# print(GetForegroundWindow())

# import os
# from pynput.keyboard import Listener as kb
# from pynput.mouse import Listener as ms
from win32gui import GetWindowText, GetForegroundWindow
import time 

# def on_key_release(key):
    # if str(key) == 'Key.alt_l':
        # getwindow()

# def on_click(x, y, button, pressed):
#     print('{0} at {1}'.format(
#             'Pressed' if pressed else 'Released',
#             (x, y)))

def getwindow():
    if GetForegroundWindow() ==  66754 or GetForegroundWindow() == 262550:
        print(GetForegroundWindow())

# with kb(on_release = on_key_release) as listener:
#     listener.join()

 
while True:
    # if GetForegroundWindow() ==  66754 or GetForegroundWindow() == 262550:
    print(GetForegroundWindow())
    time.sleep(1)