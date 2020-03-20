from builder import Builder


class MyListBuilder(Builder):
    __data = None

    def set_data(self, data):
        self.__data = [[str(x) for x in row] for row in data]

    def save_data(self):
        with open('my_data.csv', 'w') as file:
            for row in self.__data:
                file.write(','.join(row))
                file.write('\n')
