import gi
import time

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

win = Gtk.Window(title = "Vitor")
win.connect("destroy", Gtk.main_quit)

def test(widget):
        print("")

def program_quit(widget):
        print("Exiting the program ...")
        Gtk.main_quit()

box = Gtk.Box(spacing = 6)

button1 = Gtk.Button(label = "first button")
button2 = Gtk.Button(label = "second button")
button_quit = Gtk.Button(label = "exit program")

button1.connect("clicked", test)
button_quit.connect("clicked", program_quit)

box.pack_start(button1, True, True, 6)
box.pack_start(button2, True, True, 6)
box.pack_start(button_quit, True, True, 6)

win.add(box)
win.show_all()

Gtk.main()