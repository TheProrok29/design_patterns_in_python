class Singleton:
    """Implementation for one instance"""
    _instance = None

    def __new__(cls, *args, **kwargs):
        if cls._instance is None:
            instance = super().__new__(cls, *args, *kwargs)
            cls._instance = instance
        return cls._instance


# Example
if __name__ == '__main__':
    x = Singleton()
    y = Singleton()
    print(x is y)
    print(id(x))
    print(id(y))
