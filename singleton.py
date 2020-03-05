class Singleton:
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls, *args, *kwargs)
            cls._instance = instance
        return cls._instance


x = Singleton()
y = Singleton()
print(x is y)
