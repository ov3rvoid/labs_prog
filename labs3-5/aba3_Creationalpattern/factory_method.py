from abc import ABC, abstractmethod

class Product(ABC):
    @abstractmethod
    def do_something(self):
        pass

class ConcreteProductA(Product):
    def do_something(self):
        return "Product A"

class ConcreteProductB(Product):
    def do_something(self):
        return "Product B"

class Creator(ABC):
    @abstractmethod
    def factory_method(self) -> Product:
        pass
    
    def some_operation(self):
        product = self.factory_method()
        return f"Creator: {product.do_something()}"

class ConcreteCreatorA(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductA()

class ConcreteCreatorB(Creator):
    def factory_method(self) -> Product:
        return ConcreteProductB()

# Пример использования
creator_a = ConcreteCreatorA()
creator_b = ConcreteCreatorB()

print(creator_a.some_operation())  # Creator: Product A
print(creator_b.some_operation())  # Creator: Product B
