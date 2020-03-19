from abc import ABC


class Sweet(ABC):
    @classmethod
    def create_sweet(cls, *args, **kwargs):
        raise Exception('You can"t do that.')
