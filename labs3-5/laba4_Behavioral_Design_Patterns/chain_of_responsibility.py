from abc import ABC, abstractmethod

# Абстрактный обработчик
class Handler(ABC):
    @abstractmethod
    def handle_request(self, request: str):
        pass

# Конкретные обработчики
class ConcreteHandlerA(Handler):
    def handle_request(self, request: str):
        if request == "A":
            print("Handler A processed the request.")
        else:
            print("Handler A cannot process the request.")
            return None  # Передаем обработку следующему обработчику

class ConcreteHandlerB(Handler):
    def handle_request(self, request: str):
        if request == "B":
            print("Handler B processed the request.")
        else:
            print("Handler B cannot process the request.")
            return None

# Создание цепочки обработчиков
handler_a = ConcreteHandlerA()
handler_b = ConcreteHandlerB()

# Тестирование цепочки
handler_a.handle_request("A")  # Handler A processed the request.
handler_a.handle_request("B")  # Handler A cannot process the request. (должен передать в B)
handler_b.handle_request("B")  # Handler B processed the request.
