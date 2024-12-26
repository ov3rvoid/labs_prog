# Итератор
class MyIterator:
    def __init__(self, collection):
        self.collection = collection
        self.index = 0

    def __iter__(self):
        return self

    def __next__(self):
        if self.index < len(self.collection):
            result = self.collection[self.index]
            self.index += 1
            return result
        else:
            raise StopIteration

# Коллекция
class MyCollection:
    def __init__(self, items):
        self.items = items

    def __iter__(self):
        return MyIterator(self.items)

# Пример использования
collection = MyCollection([1, 2, 3, 4, 5])

for item in collection:
    print(item)
