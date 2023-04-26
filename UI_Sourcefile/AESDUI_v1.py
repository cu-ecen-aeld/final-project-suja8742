##
# Owner: Sachin Mathad
# Project: AESD Final Project
# ref: https://www.wxpython.org/pages/overview/
# ref: https://docs.wxpython.org/
# ref: https://stackoverflow.com/questions/1996518/retrieving-the-output-of-subprocess-call
##
import wx
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

        self.play_button = wx.Button(panel, label='Play')
        self.play_button.SetBackgroundColour(wx.Colour(102, 204, 102))
        self.play_button.SetForegroundColour(wx.WHITE)
        self.play_button.SetMinSize((200, 100))
        self.play_button.SetMaxSize((200, 100))

        self.pause_button = wx.Button(panel, label='Pause')
        self.pause_button.SetBackgroundColour(wx.Colour(255, 153, 51))
        self.pause_button.SetForegroundColour(wx.WHITE)
        self.pause_button.SetMinSize((200, 100))
        self.pause_button.SetMaxSize((200, 100))

        self.stop_button = wx.Button(panel, label='Stop')
        self.stop_button.SetBackgroundColour(wx.Colour(255, 51, 51))
        self.stop_button.SetForegroundColour(wx.WHITE)
        self.stop_button.SetMinSize((200, 100))
        self.stop_button.SetMaxSize((200, 100))

        hbox1.Add(self.play_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        hbox1.Add(self.pause_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)
        hbox1.Add(self.stop_button, proportion=1, flag=wx.EXPAND|wx.LEFT|wx.RIGHT, border=10)

        vbox.Add(hbox1, proportion=1, flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)
        vbox.Add(hbox2, proportion=1, flag=wx.EXPAND|wx.TOP|wx.LEFT|wx.RIGHT, border=10)

        panel.SetSizer(vbox)

        # Bind events
        self.play_button.Bind(wx.EVT_BUTTON, self.on_play)
        self.pause_button.Bind(wx.EVT_BUTTON, self.on_pause)
        self.stop_button.Bind(wx.EVT_BUTTON, self.on_stop)

        # Show the UI
        self.Show()

    # Call subprocess upon click
    def on_play(self, event):
        subprocess.call(['python', 'playback.py', 'play'])

    def on_pause(self, event):
        subprocess.call(['python', 'playback.py', 'pause'])

    def on_stop(self, event):
        subprocess.call(['python', 'playback.py', 'stop'])


if __name__ == '__main__':
    app = wx.App()
    MusicPlayer(None, title='Ausio Playback Using Bluetooth')
    app.MainLoop()
