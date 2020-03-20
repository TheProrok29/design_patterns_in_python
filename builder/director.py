from list_builder import ListBuilder
from my_list_builder import MyListBuilder


class Director:
    def __init__(self):
        self.builder = None
        self.data = None

    def set_data(self, data):
        self.data = data
        comma_exists = False
        for row in data:
            for element in row:
                element_str = str(element)
                if ',' in element_str:
                    comma_exists = True
        self.builder = MyListBuilder() if not comma_exists else ListBuilder()

    def set_builder(self, builder):
        self.builder = builder

    def create_csv(self):
        self.builder.set_data(self.data)
        self.builder.save_data()
