import gi
gi.require_version('Gtk', '3.0')
from gi.repository import Gtk

class MyWindow(Gtk.Window):

    def __init__(self):
        Gtk.Window.__init__(self, title="Hola mundo")

        self.label = Gtk.Label("¡Hola mundo!")
        self.add(self.label)

win = MyWindow()
win.connect("delete-event", Gtk.main_quit)
win.set_default_size(400,400)
win.show_all()
Gtk.main()
