from children_chair_factory import ChildrenChairsFactory
from exclusive_chair_factory import ExclusiveChairsFactory
from office_chair_factory import OfficeChairsFactory
from plane_chair_factory import PlaneChairsFactory


class UniversalFactory:
    @staticmethod
    def get_factory(type_):
        if type_ == 'normal':
            return OfficeChairsFactory()
        elif type_ == 'exclusive':
            return ExclusiveChairsFactory()
        elif type_ == 'plane':
            return PlaneChairsFactory()
        elif type_ == 'children':
            return ChildrenChairsFactory()
        else:
            return OfficeChairsFactory()
