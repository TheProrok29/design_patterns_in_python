class Chair:
    def __init__(self):
        self.back = None
        self.arms = None
        self.wheels = None
        self.base = None
        self.gas_lift = None
        self.seat = None

    def __str__(self):
        back_text = f'A chair with a size back {self.back.size}, '
        arms_text = f'armrest size {self.arms[0].size} and color {self.arms[0].color}, '
        wheels_text = ''
        if self.wheels:
            wheels_text = f'wheels color {self.wheels[0].color}, '
        base_text = f'stand made of material {self.base.material}, '
        gas_lift_text = ''
        if self.gas_lift:
            gas_lift_text = f'lifter made of material {self.gas_lift.material}. '
        seat_text = f'seat made of material {self.seat.material} and color {self.seat.color} and size {self.seat.size} '
        text_list = [back_text, arms_text, wheels_text, base_text, gas_lift_text, seat_text]
        main_text = ''.join(text_list)
        return main_text
