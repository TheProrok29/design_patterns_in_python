from functional_design_patterns.chain_of_responsibility.event_widget_example.widget import Widget


class Dialog(Widget):
    @staticmethod
    def handle_ok(event):
        print(f'Accepted by event: {event}')

    @staticmethod
    def handle_cancel(event):
        print(f'Canceled by event: {event}')

    @staticmethod
    def handle_send(event):
        print(f'Send by event: {event}')
