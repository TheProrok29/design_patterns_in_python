from functional.chain_of_responsibility.abstract_based_example.team_member import TeamMember


class Director(TeamMember):
    def process(self, task):
        if 'meet' in task:
            if 'president' in task:
                self.meet_the_president()
                return True
            elif 'minister' in task:
                self.meet_the_prime_minister()
                return True
        return False

    @staticmethod
    def meet_the_president():
        print('Meet the president')

    @staticmethod
    def meet_the_prime_minister():
        print('Meet the Prime Minister')
