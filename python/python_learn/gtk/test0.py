import gi

gi.require_version("Gtk", "3.0")        #it used to specify which version of gtk we want to use
from gi.repository import Gtk

win = Gtk.Window()                      # Create a empty windows
win.connect("destroy", Gtk.main_quit)   # That line is used to connecting to the window's delete event to ensure that the application is terminated if we click on the x to close the windows
win.show_all()                          # Used to display the window
Gtk.main()                              # Used to loop the window