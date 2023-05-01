##
# Owner: Sachin Mathad
# Project: AESD Final Project
# ref: https://www.wxpython.org/pages/overview/
# ref: https://docs.wxpython.org/
# ref: https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call
##
import wx
from wx import Bitmap
import subprocess
import sys


class MusicPlayer(wx.Frame):

    def __init__(self, parent, title):

        super(MusicPlayer, self).__init__(parent, title=title, size=(720, 200))

        # Create the UI

        panel = wx.Panel(self)

        vbox = wx.BoxSizer(wx.VERTICAL)

        hbox1 = wx.BoxSizer(wx.HORIZONTAL)

        hbox2 = wx.BoxSizer(wx.HORIZONTAL)

        # Add heading

        font = wx.Font(14, wx.FONTFAMILY_DEFAULT, wx.FONTSTYLE_NORMAL, wx.FONTWEIGHT_BOLD)

        heading = wx.StaticText(panel, label="Audio Playback Using Bluetooth")

        heading.SetFont(font)
        vbox.Add(heading, 0, wx.ALIGN_CENTER|wx.TOP|wx.BOTTOM, 10)

        self.play_button = wx.BitmapButton(panel, bitmap=Bitmap("play.png"))

        # self.pause_button = wx.BitmapButton(panel, bitmap=Bitmap("pause.png"))

        self.previous_button = wx.BitmapButton(panel, bitmap=Bitmap("previous.png"))

        self.next_button = wx.BitmapButton(panel, bitmap=Bitmap("next.png"))

        self.stop_button = wx.BitmapButton(panel, bitmap=Bitmap("stop.png"))

        hbox1.Add(self.play_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        # hbox1.Add(self.pause_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        hbox1.Add(self.previous_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        hbox1.Add(self.next_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        hbox1.Add(self.stop_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        vbox.Add(hbox1, proportion=1, flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)

        vbox.Add(hbox2, proportion=1, flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)

        # Bind events

        self.play_button.Bind(wx.EVT_BUTTON, self.on_play)

        # self.pause_button.Bind(wx.EVT_BUTTON, self.on_pause)

        self.previous_button.Bind(wx.EVT_BUTTON, self.on_previous)

        self.next_button.Bind(wx.EVT_BUTTON, self.on_next)

        self.stop_button.Bind(wx.EVT_BUTTON, self.on_stop)

        self.Show()

    def on_play(self, event):

        subprocess.call(['python', 'client_new.py', '1'])


    def on_stop(self, event):

        subprocess.call(['python', 'client_new.py', '4'])

    def on_previous(self, event):

        subprocess.call(['python', 'client_new.py', '2'])

    def on_next(self, event):

        subprocess.call(['python', 'client_new.py', '3'])

if __name__ == '__main__':

    app = wx.App()
    MusicPlayer(None, title='Ausio Playback Using Bluetooth')
    app.MainLoop()



