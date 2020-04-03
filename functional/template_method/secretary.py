from functional.template_method.worker import Worker


class Secretary(Worker):

    def prepare_for_work(self):
        print('Prepare secretary for work')

    def go_to_work(self):
        print('Go to secretary work')

    def start_up(self):
        print('Start work as secretary')

    def do_work(self):
        print('Call someone')
