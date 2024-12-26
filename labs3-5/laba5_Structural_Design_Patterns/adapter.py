# Цель
class Target:
    def request(self):
        return "Target: The default behavior."

# Несовместимый класс
class Adaptee:
    def specific_request(self):
        return "Adaptee: Specific behavior."

# Адаптер
class Adapter(Target):
    def __init__(self, adaptee):
        self._adaptee = adaptee

    def request(self):
        return self._adaptee.specific_request()

# Пример использования
target = Target()
print(target.request())  # Target: The default behavior.

adaptee = Adaptee()
adapter = Adapter(adaptee)
print(adapter.request())  # Adaptee: Specific behavior.
