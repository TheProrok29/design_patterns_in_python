from team_member import TeamMember


class Secretary(TeamMember):
    def process(self, task):
        if 'call' in task:
            self.call()
            return True
        if 'write' in task and 'back' in task:
            self.write_back()
            return True
        if 'tea' in task:
            self.get_tea()
            return True
        return False

    @staticmethod
    def call():
        print('Call')

    @staticmethod
    def write_back():
        print('Write back message')

    @staticmethod
    def get_tea():
        print('Get tea')
