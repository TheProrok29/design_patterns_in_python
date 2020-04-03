from datetime import datetime

from other_design_patterns.lazy_initialization.engine import Engine


class Car:
    def __init__(self, model, engine_type):
        self.model = model
        self.engine_type = engine_type
        self.engine = None
        self.year = datetime.now().year

    def take_a_look(self, observer):
        print(f'{observer} is taking a look at {self.model}')

    def request_additional_informations(self):
        print(f'That car has a {self.engine_type} engine type. '
              f'It is {self.model} from {self.year}')

    def test_drive(self, observer):
        if self.engine is None:
            self.engine = Engine(self.engine_type)
        print(f'{observer} is testing the car...')
