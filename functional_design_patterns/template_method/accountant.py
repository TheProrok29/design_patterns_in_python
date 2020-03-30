from worker import Worker


class Accountant(Worker):

    def prepare_for_work(self):
        print('Prepare accountant for work')

    def go_to_work(self):
        print('Go to accountant work')

    def start_up(self):
        print('Run the excel')

    def do_work(self):
        print('Check some bills')
