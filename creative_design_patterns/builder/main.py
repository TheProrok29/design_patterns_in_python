from creative_design_patterns.builder.director import Director

data = [
    ['Jan', 'Kowalski', 27, '111 - 222 - 333', 'Poland'],
    ['John', 'Smith', 33, '333 - 222 - 111', 'England'],
    ['Martin', 'Aub', 7, None, 'France'],
]

data2 = [
    {'name': 'Jan', 'surname': 'Kowalski', 'age': 27, 'phone': '111 - 222 - 333', 'country': 'Poland'},
    {'name': 'John', 'surname': 'Smith', 'age': 33, 'phone': '333 - 222 - 111', 'country': 'England'},
    {'name': 'Martin', 'surname': 'Aub', 'age': 7, 'phone': None, 'country': 'France'},
]

director = Director()
director.set_data(data)
director.create_csv()
