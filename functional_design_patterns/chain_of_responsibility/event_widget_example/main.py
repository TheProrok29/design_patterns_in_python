from functional_design_patterns.chain_of_responsibility.event_widget_example.dialog import Dialog
from functional_design_patterns.chain_of_responsibility.event_widget_example.event import Event
from functional_design_patterns.chain_of_responsibility.event_widget_example.window import Window

my_window = Window()
my_dialog = Dialog(parent=my_window)

event = Event('ok')
my_dialog.handle(event)

event = Event('close')
my_dialog.handle(event)

event = Event('closesdsdgfdrf')
my_dialog.handle(event)
