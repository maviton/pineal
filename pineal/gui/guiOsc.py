from threading import Thread
import gtk
from thirdparty.OSC import OSCClient, OSCServer, OSCMessage
from pineal.config import OSC_CORE, OSC_GUI

class GuiOsc(Thread):
    def __init__(self, gui):
        Thread.__init__(self)
        self.gui = gui

        self.server = OSCServer(OSC_GUI)
        self.server.addMsgHandler('/add', self.add)
        self.server.addMsgHandler('/error', self.error)

        self.client = OSCClient()
        self.client.connect(OSC_CORE)

    def run(self):
        self.server.serve_forever()

    def add(self, path, tags, args, source):
        self.gui.add(*args)

    def error(self, path, tags, args, source):
        name, log = args
        if log:
            print name, log

    def send_change(self, visual, var, value):
        self.client.send( OSCMessage('/visual/'+visual+'/'+var, float(value)) )