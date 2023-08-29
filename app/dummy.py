# -*- coding: iso-8859-15 -*-

class DummyHandler(object):
    def __init__(self, event):
        self.event = event

    def process(self):
        return 'Just for fun!', 200
