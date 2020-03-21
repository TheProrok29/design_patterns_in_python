class Director:

    def __init__(self, builder):
        self.builder = builder

    def ask_for_chair(self):
        return self.builder.create_chair()
