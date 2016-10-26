#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
__author__ = 'wangjj'
__mtime__ = '20161025下午 11:56'


class hello_world(wx.Frame):

    def __init__(self, superior):
        super(hello_world, self).__init__(
            parent=superior,
            title='hello world in wxPython',
        )
        self.panel = wx.Panel(self)
        self.sizer = wx.BoxSizer(wx.VERTICAL)
        self.text_1 = wx.TextCtrl(
            self.panel,
            value='hello,world!',
            size=(200, 180),
            style=wx.TE_MULTILINE
        )
        self.sizer.Add(self.text_1, 0, wx.ALIGN_TOP | wx.EXPAND)
        self.button = wx.Button(self.panel, label='click me')
        self.sizer.Add(self.button)
        self.panel.SetSizerAndFit(self.sizer)
        self.panel.Layout()
        self.Bind(wx.EVT_BUTTON, self.on_click, self.button)

    def on_click(self,text):
        self.text_1.AppendText('\nhello,world!')

if __name__ == '__main__':
    app = wx.App()
    Hello_World = hello_world(None)
    Hello_World.Show(True)
    app.MainLoop()
