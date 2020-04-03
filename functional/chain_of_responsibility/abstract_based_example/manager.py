from functional.chain_of_responsibility.abstract_based_example.team_member import TeamMember


class Manager(TeamMember):
    def process(self, task):
        if 'find' in task:
            self.find_someone()
            return True
        if 'task' in task:
            self.add_task()
            return True
        if 'check' in task and 'process' in task:
            self.check_the_process()
            return True
        return False

    @staticmethod
    def find_someone():
        print('Find a worker')

    @staticmethod
    def add_task():
        print('Add task to someone')

    @staticmethod
    def check_the_process():
        print('Check toe process')
