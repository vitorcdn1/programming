import gi

gi.require_version("Gtk", "3.0")
from gi.repository import Gtk

def test(widget):
        for c in range(0, 10):
                print("Hello World")

        win.set_title("test")
        
        if button1.get_label() != "click on me":
                button1.set_label("click on me")
        else:
                button1.set_label("you just clicked on me")

def test1(widget):
        print("i'm the second button")
        for c in dir(button1.props):
                print(c)

def program_quit(widget):
        Gtk.main_quit()

win = Gtk.Window(title = "Vitor")
win.connect("destroy", Gtk.main_quit)

#button = Gtk.Button(label = "click on me")
#button.connect("clicked", test)
#win.add(button)

box = Gtk.Box(spacing = 6)

button1 = Gtk.Button(label = "First Button")
button2 = Gtk.Button(label = "Second Button")
button_quit = Gtk.Button(label = "Sair do programa")

button1.connect("clicked", test)
button2.connect("clicked", test1)
button_quit.connect("clicked", program_quit)

box.pack_start(button2, True, True, 0)
box.pack_start(button1, True, True, 0)
box.pack_start(button_quit, True, True, 0)

win.add(box)


win.show_all()
Gtk.main()