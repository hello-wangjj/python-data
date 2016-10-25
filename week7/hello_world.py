#!/usr/bin/env python
# -*- coding: utf-8 -*-
import wx
__author__ = 'wangjj'
__mtime__ = '20161025下午 8:46'


class Frame1(wx.Frame):

    # noinspection PyUnresolvedReferences
    def __init__(self, superior):
        super(Frame1, self).__init__(parent=superior, title='Example',
                                     pos=(100, 200),
                                     size=(500, 400))
        # one
        self.panel = wx.Panel(self)
        # self.text = wx.TextCtrl(self.panel, value='hello world!',
        #                         size=(200, 100))
        # 另一个
        self.panel.Bind(wx.EVT_LEFT_UP, self.on_click)

        # wx.Frame.__init__(
        #     self, parent=superior, title="Example", pos=(
        #         100, 200), size=(
        #         200, 100))
        # panel = wx.Panel(self)
        # text1 = wx.TextCtrl(panel, value="Hello, World!", size=(200, 100))
    def on_click(self, event):
        pos_mouse = event.GetPosition()
        wx.StaticText(
            parent=self.panel,
            label=str(pos_mouse.x) + ',' + str(pos_mouse.y),
            pos=(
                pos_mouse.x,
                pos_mouse.y))
if __name__ == '__main__':
    app = wx.App()
    frame = Frame1(None)
    frame.Show(True)
    app.MainLoop()
