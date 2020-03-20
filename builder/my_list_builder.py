from builder import Builder


class MyListBuilder(Builder):
    __data = None

    def set_data(self, data):
        pass

    def save_data(self):
        with open('my_data.csv', 'w') as file:
            for row in self.__data:
                file.write(','.join(row))
                file.write('\n')
