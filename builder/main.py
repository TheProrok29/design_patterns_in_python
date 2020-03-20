from list_builder import ListBuilder
from my_list_builder import MyListBuilder

data = [
    ['Jan', 'Kowalski', 27, '111 - 222 - 333', 'Poland'],
    ['John', 'Smith', '33, 333 - 222 - 111', 'England'],
    ['Martin', 'Aub', 7, None, 'France'],
]

builder1, builder2 = ListBuilder(), MyListBuilder()

builder1.set_data(data)
builder2.set_data(data)
builder1.save_data()
builder2.save_data()
