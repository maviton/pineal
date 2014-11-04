from time import sleep
import gtk

from pineal.gui.guiOsc import GuiOsc
from pineal.gui.widgets import VisualFrame, Menu


class Gui(object):
    """Display a gui"""
    def __init__(self):
        self.win = gtk.Window()
        self.win.set_title('Pineal Loop Project')
        self.win.resize(200,1)
        self.win.connect('delete-event', self.quit)

        vbox = gtk.VBox()
        menu = Menu(self)
        self.box = gtk.HBox()

        self.win.add(vbox)
        vbox.add(menu)
        vbox.add(self.box)

        self.win.show_all()

        self.visuals = {}
        self._stop = False

    def run(self):
        print 'starting pineal.gui'
        self.guiOsc = GuiOsc(self)
        self.guiOsc.start()

        try:
            while not self._stop:
                gtk.main_iteration()
                sleep(0.01)  # don't ask me why
        except KeyboardInterrupt:
            self.guiOsc.stop()

    def stop(self):
        print 'stopping pineal.gui'
        self._stop = True

    def quit(self, widget, event):
        return not self._stop

    def add(self, visual, var, value):
        with gtk.gdk.lock:
            if visual not in self.visuals.keys():
                self.visuals[visual] = VisualFrame(self, visual)
                self.box.add(self.visuals[visual])

            if var not in self.visuals[visual].variables.keys():
                self.visuals[visual].add_var(var)
                self.visuals[visual].variables[var].change(value)

            self.box.show_all()
