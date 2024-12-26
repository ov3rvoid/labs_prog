from abc import ABC, abstractmethod

# Реализация: разные способы рисования
class DrawingTool(ABC):
    @abstractmethod
    def draw(self, shape):
        pass

class Brush(DrawingTool):
    def draw(self, shape):
        print(f"Drawing {shape} with a brush")

class Pencil(DrawingTool):
    def draw(self, shape):
        print(f"Drawing {shape} with a pencil")

# Абстракция: разные виды форм
class Shape(ABC):
    def __init__(self, drawing_tool: DrawingTool):
        self.drawing_tool = drawing_tool

    @abstractmethod
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        self.drawing_tool.draw("circle")

class Square(Shape):
    def draw(self):
        self.drawing_tool.draw("square")

# Создание объектов
brush = Brush()
circle = Circle(brush)
square = Square(brush)

circle.draw()  # Drawing circle with a brush
square.draw()  # Drawing square with a brush

# Смена инструмента
pencil = Pencil()
circle.drawing_tool = pencil
circle.draw()  # Drawing circle with a pencil
