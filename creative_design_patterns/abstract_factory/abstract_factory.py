from factories import *


class UniversalFactory:
    @staticmethod
    def get_factory(type_):
        return globals()[type_]()
