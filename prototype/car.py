class Car:
    def __init__(self, brand, model, engine, gearbox, body_type, license_plate, owner, **kwargs):
        self.brand = brand
        self.model = model
        self.engine = engine
        self.gearbox = gearbox
        self.body_type = body_type
        self.license_plate = license_plate
        self.owner = owner
        for key in kwargs:
            setattr(self, key, kwargs[key])

    def __str__(self):
        summary = []
        for key, val in vars(self).items():
            summary.append(f'{key}: {val}\n')

        return summary
