import wx
import pyperclip
import re
import sys
import os
import wx.adv

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

def shorten_amazon_url(event):
    LongURL = pyperclip.paste()

    if 'amazon' in LongURL:
        TempStr = re.split('/|\?', LongURL)
        ShortURL = 'https://www.amazon.co.jp/dp/' + TempStr[5] + '/'
        pyperclip.copy(ShortURL)


class TaskbarIcon(wx.adv.TaskBarIcon):
    def __init__(self):
        super(TaskbarIcon, self).__init__()
        self.icon = wx.Icon(resource_path("Amazon_icon.ico"), wx.BITMAP_TYPE_ICO)
        self.SetIcon(self.icon, "Amazon URL Shorter Ver.1.0.0")
        self.Bind(wx.adv.EVT_TASKBAR_LEFT_DOWN, self.on_left_down)

    def CreatePopupMenu(self):
        menu = wx.Menu()
        menu.Append(1, "Amazon URL Shorter")
        menu.Append(2, "終了")
        self.Bind(wx.EVT_MENU, shorten_amazon_url, id=1)
        self.Bind(wx.EVT_MENU, self.on_exit, id=2)
        return menu

    def on_left_down(self, event):
        shorten_amazon_url(self)

    def on_exit(self, event):
        self.RemoveIcon()
        self.Destroy()
        sys.exit()


if __name__ == '__main__':
    app = wx.App()
    TaskbarIcon()
    app.MainLoop()

