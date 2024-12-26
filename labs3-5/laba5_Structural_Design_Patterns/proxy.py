# Интерфейс
class RealSubject:
    def request(self):
        print("RealSubject: Handling request.")

# Прокси
class Proxy:
    def __init__(self, real_subject: RealSubject):
        self._real_subject = real_subject

    def request(self):
        print("Proxy: Checking access before forwarding request.")
        self._real_subject.request()
        print("Proxy: Logging request after forwarding.")

# Пример использования
real_subject = RealSubject()
proxy = Proxy(real_subject)

proxy.request()