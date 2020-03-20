class Director:
    def __init__(self, builder):
        self.builder = builder

    def set_builder(self, builder):
        self.builder = builder

    def create_csv(self, data):
        self.builder.set_data(data)
        self.builder.save_data()
