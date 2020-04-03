from copy import deepcopy


class Prototype:
    def __init__(self):
        self.objs = dict()

    def add_prototype(self, id_, obj):
        self.objs[id_] = obj

    def del_prototype(self, id_):
        del self.objs[id_]

    def clone(self, id_, **kwargs):
        if id_ in self.objs:
            instance = deepcopy(self.objs[id_])
            for key in kwargs:
                setattr(instance, key, kwargs[key])
            return instance
        else:
            raise ModuleNotFoundError
