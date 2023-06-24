import rumps
import pyperclip
import re
import sys
import os

def resource_path(relative_path):
    if hasattr(sys, '_MEIPASS'):
        return os.path.join(sys._MEIPASS, relative_path)
    return os.path.join(os.path.abspath("."), relative_path)

class URLShoter(rumps.App):
    @rumps.clicked('Amazon URL Shorter')
    def get_URLShoter(self, _):
        LongURL = pyperclip.paste()

        if 'amazon' in LongURL:
            TempStr = re.split('/|\?', LongURL)
            ShortURL = 'https://www.amazon.co.jp/dp/' + TempStr[5] + '/'
            pyperclip.copy(ShortURL)

if __name__ == '__main__':
    # IconPath = resource_path + '/Amazon_icon.png'
    IconPath = '/Users/rautie/work/Python/AmazonURLShorter/Amazon_icon.png'
    URLShoter('Rumps Test', icon=IconPath, quit_button='終了').run()
