from whole_sale_builder import WholeSaleBuilder
from handmade_builder import HandmadeBuilder
from director import Director

director = Director(HandmadeBuilder())
chair = director.ask_for_chair()
print(chair)
