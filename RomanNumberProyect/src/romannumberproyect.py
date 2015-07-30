#!/usr/bin/env python
# -*- coding: utf-8 -*-
__author__ = "JuanDavid"
__date__ = "$29/07/2015 08:44:56 PM$"

from gui.window import Window

if __name__ == "__main__":
    try:
        window = Window()
    except Exception as e:
        print e.message