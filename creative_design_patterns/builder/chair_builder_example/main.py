from creative_design_patterns.builder.chair_builder_example.director import Director
from creative_design_patterns.builder.chair_builder_example.handmade_builder import HandmadeBuilder

director = Director(HandmadeBuilder())
chair = director.ask_for_chair()
print(chair)
