import psutil
import win32gui
import win32api
import win32con
import win32process

def GetWindowList():
    """
    returns window title list
    based on this answer - https://stackoverflow.com/a/31280850
    """

    titles = []
    t = []
    pidList = [(p.pid, p.name()) for p in psutil.process_iter()]
    print(len(pidList))
    def enumWindowsProc(hwnd, lParam):
        """ append window titles which match a pid """
        if (lParam is None) or ((lParam is not None) and (win32process.GetWindowThreadProcessId(hwnd)[1] == lParam)):
            text = win32gui.GetWindowText(hwnd)
            if text:
                wStyle = win32api.GetWindowLong(hwnd, win32con.GWL_STYLE)
                if wStyle & win32con.WS_VISIBLE:
                    t.append("%s" % (text))
                    return

    def enumProcWnds(pid=None):
        win32gui.EnumWindows(enumWindowsProc, pid)

    for pid, pName in pidList:
        enumProcWnds(pid)
        if t:
            for title in t:
                titles.append("('{0}', '{1}')".format(pName, title))
            t = []

    titles = sorted(titles, key=lambda x: x[0].lower())
    return titles

t =GetWindowList()
for i in t :
    print(i)