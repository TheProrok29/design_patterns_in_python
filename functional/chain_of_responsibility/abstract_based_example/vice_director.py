from functional.chain_of_responsibility.abstract_based_example.team_member import TeamMember


class ViceDirector(TeamMember):
    def process(self, task):
        if 'meet' in task:
            if 'president' in task:
                self.meet_someone_else()
                return True
            if 'sign' in task:
                self.sign_documents()
                return True
        return False

    @staticmethod
    def meet_someone_else():
        print('Meet')

    @staticmethod
    def sign_documents():
        print('Sign documents')
