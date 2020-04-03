from functional.chain_of_responsibility.abstract_based_example.team_member import TeamMember


class Worker(TeamMember):
    def process(self, task):
        if 'work' in task:
            self.do_work()
            return True
        return False

    @staticmethod
    def do_work():
        print('Do work')
