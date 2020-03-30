from widget import Widget


class Window(Widget):
    @staticmethod
    def handle_close(event):
        print(f'Window closed by event: {event}')
