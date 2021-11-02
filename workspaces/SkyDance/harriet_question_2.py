#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

src_path = './src'

if not src_path in sys.path:
    sys.path.append(src_path)


from events import _events


def receiveEvent(event_type, *args, **kwargs):
    events = _events()
    events.get(event_type)(args, kwargs)


receiveEvent("New Asset", name='Char_LookDev', user='harriet.landa', path='/Users/haarrii/Documents/skydance', text='This is a text test', mail=1, )