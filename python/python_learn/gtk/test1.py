import gi

gi.require_version("Gtk", "3.0")

from gi.repository import Gtk

win = Gtk.Window(title = "Grid")
win.connect("destroy", Gtk.main_quit)

grid = Gtk.Grid()
win.add(grid)

button1 = Gtk.Button(label = "Button1")
button2 = Gtk.Button(label = "Button2")
button3 = Gtk.Button(label = "Button3")
button4 = Gtk.Button(label = "Button4")
button5 = Gtk.Button(label = "Button5")
button6 = Gtk.Button(label = "Button6")

grid.add(button1)
grid.attach(button2, 1, 0, 1, 1)
grid.attach(button3, 0, 1, 2, 1)
grid.attach(button4, 2, 0, 1, 2)

win.show_all()
Gtk.main()