from functional_design_patterns.strategy.point_distance_strategy.transport_chooser import TransportChooser

a = (1, 1)
b = (5, 5)
chooser = TransportChooser(a, b)
chooser.use_strategy()
