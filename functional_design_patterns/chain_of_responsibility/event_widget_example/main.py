from dialog import Dialog
from event import Event
from window import Window

my_window = Window()
my_dialog = Dialog(parent=my_window)

event = Event('ok')
my_dialog.handle(event)

event = Event('close')
my_dialog.handle(event)

event = Event('closesdsdgfdrf')
my_dialog.handle(event)
