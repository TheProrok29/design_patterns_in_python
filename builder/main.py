from director import Director

data = [
    ['Jan', 'Kowalski', 27, '111 - 222 - 333', 'Poland'],
    ['John', 'Smith', 33, '333 - 222 - 111', 'England'],
    ['Martin', 'Aub', 7, None, 'France'],
]

director = Director()
director.set_data(data)
director.create_csv()
