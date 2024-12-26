from abc import ABC, abstractmethod

# Стратегия
class PaymentStrategy(ABC):
    @abstractmethod
    def pay(self, amount: float):
        pass

# Конкретные стратегии
class CreditCardPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using Credit Card.")

class PayPalPayment(PaymentStrategy):
    def pay(self, amount: float):
        print(f"Paid {amount} using PayPal.")

# Контекст
class ShoppingCart:
    def __init__(self, payment_strategy: PaymentStrategy):
        self.payment_strategy = payment_strategy

    def checkout(self, amount: float):
        self.payment_strategy.pay(amount)

# Пример использования
cart = ShoppingCart(CreditCardPayment())
cart.checkout(100)  # Paid 100 using Credit Card.

cart.payment_strategy = PayPalPayment()
cart.checkout(200)  # Paid 200 using PayPal.
