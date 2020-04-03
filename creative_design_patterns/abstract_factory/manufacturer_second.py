from creative_design_patterns.abstract_factory.abstract_manufacturer import Manufacturer


class ChairY(Manufacturer):
    @staticmethod
    def make_a_call():
        print('Chair was produced')

    def produce_chair(self):
        a_chair = super().produce_chair()
        self.make_a_call()
        return a_chair
