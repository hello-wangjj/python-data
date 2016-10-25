#!/usr/bin/env python
# -*- coding: utf-8 -*-
from pylab import mpl
__author__ = 'wangjj'
__mtime__ = '20161025上午 11:03'


def set_ch():
    mpl.rcParams['font.sans-serif'] = ['FangSong']  # 指定默认字体
    mpl.rcParams['axes.unicode_minus'] = False  # 解决保存图像是负号'-'显示为方块的问题
