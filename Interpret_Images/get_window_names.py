import win32gui
import win32ui
import win32con

def get_window_names():
    names = []
    def winEnumHandler(hwnd, ctx):
        if win32gui.IsWindowVisible(hwnd):
            names.append(win32gui.GetWindowText(hwnd))
    win32gui.EnumWindows(winEnumHandler, None)
    return names