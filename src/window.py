
from gi.repository import Gtk


@Gtk.Template(resource_path='/org/example/App/window.ui')
class CovidtrackingWindow(Gtk.ApplicationWindow):
    __gtype_name__ = 'CovidtrackingWindow'

    label = Gtk.Template.Child()

    def __init__(self, **kwargs):
        super().__init__(**kwargs)
