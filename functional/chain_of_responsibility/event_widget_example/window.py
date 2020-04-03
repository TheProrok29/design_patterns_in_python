from functional.chain_of_responsibility.event_widget_example.widget import Widget


class Window(Widget):
    @staticmethod
    def handle_close(event):
        print(f'Window closed by event: {event}')
