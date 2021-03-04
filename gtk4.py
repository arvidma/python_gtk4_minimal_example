from gi import require_version
require_version('Gtk', '4.0')
from gi.repository import Gtk, Gio


class TheApp(Gtk.Application):
    application_id = "se.rvid.gtk4mini"

    def __init__(self, *args, **kwargs):
        super().__init__(*args, application_id=self.application_id)  # Must call parent
        self.window = None  # The app should have a window.

    def do_activate(self):
        """ 
        The application must be activated. It can be done with method with
        this exact name, or by connecting a signal handler to the "activate"
        signal of the app.
        """
        Gtk.Application.do_startup(self)  # Must call parent

        # This is where we initialize our window.
        self.window = Gtk.Window(application=self,
                                 title="A window")
        label = Gtk.Label()
        label.set_markup("<b>Look, a label!</b>")

        # Windows only have one child, usually a container of some sort, but
        # for this example a label will do.
        self.window.set_child(label)

        # For the sake of all that is holy, don't forget to present yourself.
        self.window.present()


app = TheApp()
app.run()

