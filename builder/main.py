from director import Director
from list_builder import ListBuilder
from my_list_builder import MyListBuilder

data = [
    ['Jan', 'Kowalski', 27, '111 - 222 - 333', 'Poland'],
    ['John', 'Smith', 33, '333 - 222 - 111', 'England'],
    ['Martin', 'Aub', 7, None, 'France'],
]

director = Director(ListBuilder())
director.create_csv(data)
director.set_builder(MyListBuilder())
director.create_csv(data)
