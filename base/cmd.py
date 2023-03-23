 #打开浏览器
import subprocess

class Cmd:
    def open_Google(self):
        subprocess.check_call('chrome.exe --remote-debugging-port=9527 --user-data-dir="F:\selenium\AutomationProfile"', cwd='C:\Program Files\Google\Chrome\Application')