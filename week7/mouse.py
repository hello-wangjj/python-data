#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
__author__ = 'wangjj'
__mtime__ = '20161025下午 8:18'


class MyApp(wx.App):

    def __init__(self):
        super(MyApp, self).__init__()
    #     self.frame = wx.Frame(None, title='hello world!')
    #     self.frame.Show()

    def OnPreInit(self):
        frame = wx.Frame(None, title='hello world!')
        frame.Show()
        return True

if __name__ == '__main__':
    app = MyApp()
    app.MainLoop()
