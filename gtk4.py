import sys

import gi
gi.require_version('Gtk', '4.0')  # Must be done before importing Gtk.
from gi.repository import Gtk


class TheApp(Gtk.Application):

    def __init__(self, **kwargs):
        # Must call parent. The application id doubles as the single-instance
        # identity: launching the app again activates the existing instance.
        super().__init__(application_id="se.rvid.gtk4mini", **kwargs)

    def do_activate(self):
        """
        The application must be activated. It can be done with a method with
        this exact name, or by connecting a signal handler to the "activate"
        signal of the app.

        Activation can happen more than once (e.g. when the app is launched
        a second time), so reuse the window if we already have one.
        """
        window = self.props.active_window
        if window is None:
            # This is where we initialize our window. ApplicationWindow ties
            # the window's lifetime to the application.
            window = Gtk.ApplicationWindow(application=self, title="A window")

            label = Gtk.Label()
            label.set_markup("<b>Look, a label!</b>")

            # Windows only have one child, usually a container of some sort,
            # but for this example a label will do.
            window.set_child(label)

        # For the sake of all that is holy, don't forget to present yourself.
        window.present()


if __name__ == "__main__":
    app = TheApp()
    sys.exit(app.run(sys.argv))
