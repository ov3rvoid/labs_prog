class Singleton:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
        return cls._instance

# Пример использования
singleton1 = Singleton()
singleton2 = Singleton()

print(singleton1 is singleton2)  # True, т.к. оба объекта ссылаются на один и тот же экземпляр
