class Product:
    def __init__(self):
        self.parts = []

    def add_part(self, part):
        self.parts.append(part)

    def show_parts(self):
        return ', '.join(self.parts)

class Builder:
    def __init__(self):
        self.product = Product()

    def build_part_a(self):
        self.product.add_part("Part A")

    def build_part_b(self):
        self.product.add_part("Part B")

    def build_part_c(self):
        self.product.add_part("Part C")

    def get_result(self):
        return self.product

class Director:
    def __init__(self, builder):
        self.builder = builder

    def construct(self):
        self.builder.build_part_a()
        self.builder.build_part_b()
        self.builder.build_part_c()

# Пример использования
builder = Builder()
director = Director(builder)
director.construct()

product = builder.get_result()
print(product.show_parts())  # Part A, Part B, Part C
