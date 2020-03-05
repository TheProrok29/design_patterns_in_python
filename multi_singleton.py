class MultiSingleton:
    """Implementation for exact quantity instances"""
    _instances = []
    _instances_max = 3
    _instances_actual = -1

    def __new__(cls, *args, **kwargs):
        if len(cls._instances) < cls._instances_max:
            instance = super().__new__(cls, *args, *kwargs)
            cls._instances.append(instance)
        cls._instances_actual += 1
        cls._instances_actual = cls._instances_actual % 3
        return cls._instances[cls._instances_actual]
