import csv


class MenuModel:
    def __init__(self):
        self.file = 'menu.csv'
        self.temp_menu = csv.DictReader(open(self.file, encoding='UTF-8'))
        self.menu = []
        for row in self.temp_menu:
            dictionary = dict()
            dictionary['Name'] = row['Name']
            dictionary['Price'] = row['Price']
            dictionary['Count'] = row['Count']
            dictionary['Availability'] = row['Availability']
            self.menu.append(dictionary)

    def get_meal(self, name):
        meal_exist = False
        meal_availability = False
        for row in self.menu:
            if row['Name'] == name:
                meal_exist = True
                meal_availability = int(row['Availability'])
        if meal_exist and meal_availability:
            return name
        else:
            return None

    def get_menu(self):
        menu_to_return = []
        for row in self.menu:
            menu_to_return.append((row['Name'], row['Count'], row['Price']))
        return menu_to_return
