from abc import ABC, abstractmethod

class AbstractProductA(ABC):
    @abstractmethod
    def do_something(self):
        pass

class AbstractProductB(ABC):
    @abstractmethod
    def do_something(self):
        pass

class ProductA1(AbstractProductA):
    def do_something(self):
        return "ProductA1"

class ProductB1(AbstractProductB):
    def do_something(self):
        return "ProductB1"

class ProductA2(AbstractProductA):
    def do_something(self):
        return "ProductA2"

class ProductB2(AbstractProductB):
    def do_something(self):
        return "ProductB2"

class AbstractFactory(ABC):
    @abstractmethod
    def create_product_a(self) -> AbstractProductA:
        pass

    @abstractmethod
    def create_product_b(self) -> AbstractProductB:
        pass

class ConcreteFactory1(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA1()

    def create_product_b(self) -> AbstractProductB:
        return ProductB1()

class ConcreteFactory2(AbstractFactory):
    def create_product_a(self) -> AbstractProductA:
        return ProductA2()

    def create_product_b(self) -> AbstractProductB:
        return ProductB2()

# Пример использования
factory1 = ConcreteFactory1()
factory2 = ConcreteFactory2()

product_a1 = factory1.create_product_a()
product_b1 = factory1.create_product_b()

product_a2 = factory2.create_product_a()
product_b2 = factory2.create_product_b()

print(product_a1.do_something())  # ProductA1
print(product_b1.do_something())  # ProductB1
print(product_a2.do_something())  # ProductA2
print(product_b2.do_something())  # ProductB2
