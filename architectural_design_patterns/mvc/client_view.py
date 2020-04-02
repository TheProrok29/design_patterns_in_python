class ClientView:
    def show(self, meal):
        print(f'Here is my {meal} meal.')

    def request_meal(self):
        return input('Put here the name of a meal: ')

    def show_menu(self, menu):
        for row in menu:
            print(row)
