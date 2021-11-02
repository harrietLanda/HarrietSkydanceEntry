#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import sys

src_path = './src'

if not src_path in sys.path:
    sys.path.append(src_path)


from events import _events


def receiveEvent(event_type, *args, **kwargs):
    """Receive the event and check the events dictionary to call the actions

    Args:
        name (string): name of the file
        user (string): your user
        path (string): path where want to save the file
        text (string): text to write in the file
        mail (bool): True if want to send e-mail, False if don't
        to (string): the receiver mail account
        subject (string): mail subject
        mail_text (string): mail body text
        attach (bool): True if want to attach file on e-mail, False if don't
        attach_path (string): the path of the file that want to attach
    """
    events = _events()
    events.get(event_type)(args, kwargs)


receiveEvent("New Asset", name='Char_LookDev', user='harriet.landa', path='/Users/haarrii/Documents/skydance', text='This is a text test', mail=1, to='ximharri@gmail.com', subject='Renders', mail_text='Here are your renders', attach=0)