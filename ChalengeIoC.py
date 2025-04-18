 IoC — Inversion of Control (Kontrolün Tersine Çevrilmesi)
📌 Tanım:
Yazılım bileşenlerinin kontrolü, artık kendilerinde değil, dış bir yapı (framework, container) tarafından yönetilir.

Yani:

“Ben neyi ne zaman çalıştıracağım” yerine, “başkası beni ne zaman çağırırsa çalışırım” mantığıdır.

🤝 DI ve IoC ilişkisi

IoC	Geniş bir prensip — kontrol tersine döner
DI (Dependency Injection)	IoC’nin bir uygulama şeklidir — bağımlılıklar dışarıdan verilir
Özetle:

👉 DI, bir IoC tekniğidir.
Her DI uygulaması IoC yapar ama her IoC, DI olmak zorunda değildir.

🧠 Neden “Inversion”?
Normalde bir sınıf ihtiyacını kendi oluşturur, kendi yönetir:


class UserService:
    def __init__(self):
        self.email_service = EmailService()  # ❌ Kontrol bende
Ama IoC yaklaşımında başka bir yapı bunu senin yerine yapar ve sana verir:

class UserService:
    def __init__(self, email_service):
        self.email_service = email_service  # ✅ Kontrol dış yapıda
Sen sadece neye ihtiyacın olduğunu söylersin, nasıl verileceğiyle ilgilenmezsin.

🔧 Uygulamalı Örnek (Senin Uçuş Sistemin Üzerinden)
🧩 Bileşenler:
FlightReservationService (uçuş rezervasyonu yapar)

LoggerService (log tutar)

IoCContainer (bileşenleri oluşturur ve bağımlılıkları enjekte eder)

✅ IoC Container (Basit)

class IoCContainer:
    def __init__(self):
        self._services = {}

    def register(self, name, creator):
        self._services[name] = creator

    def resolve(self, name):
        return self._services[name]()
🚀 Servislerimizi tanımlayalım:

class LoggerService:
    def log(self, msg):
        print("[LOG]", msg)

class FlightReservationService:
    def __init__(self, logger: LoggerService):
        self.logger = logger

    def reserve(self, passenger, flight):
        self.logger.log(f"{passenger} için {flight} rezervasyonu yapıldı.")
🧪 IoC ile Kullanım:

container = IoCContainer()

# Kayıt işlemleri
container.register("logger", lambda: LoggerService())
container.register("reservation_service", lambda: FlightReservationService(container.resolve("logger")))

# Kullanım
reservation_service = container.resolve("reservation_service")
reservation_service.reserve("Ali Can", "IST123")
Burada kontrol tamamen IoCContainer’da:
Sen FlightReservationService'i doğrudan oluşturmuyorsun.
Container onu, ihtiyacı olan logger ile birlikte senin yerine oluşturuyor.

1. Adım: Temel Servisleri Tanımlayalım
LoggerService

class LoggerService:
    def log(self, message):
        print("[LOG]:", message)
EmailService

class EmailService:
    def send_confirmation(self, user):
        print(f"{user} adlı yolcuya e-posta gönderildi.")

        class PaymentService:
            def process_payment(self, user, amount):
                print(f"{user} kişisinden {amount}₺ ödeme alındı.")

                2.
                Adım: Ana
                FlightReservationService(DI
                destekli)


                class FlightReservationService:
                    def __init__(self, logger, emailer, payment):
                        self.logger = logger
                        self.emailer = emailer
                        self.payment = payment

                    def reserve(self, user, flight_no, price):
                        self.logger.log(f"{user} için {flight_no} uçuşuna rezervasyon başlatıldı.")
                        self.payment.process_payment(user, price)
                        self.emailer.send_confirmation(user)
                        self.logger.log("Rezervasyon tamamlandı.")

                        3.
                        Adım: IoC
                        Container(Singleton
                        destekli)


                        class IoCContainer:
                            def __init__(self):
                                self._services = {}
                                self._singletons = {}

                            def register(self, name, creator, singleton=False):
                                self._services[name] = (creator, singleton)

                            def resolve(self, name):
                                creator, singleton = self._services[name]
                                if singleton:
                                    if name not in self._singletons:
                                        self._singletons[name] = creator()
                                    return self._singletons[name]
                                else:
                                    return creator()
4. Adım: Bağımlılıkları Register Et

container = IoCContainer()

# Singleton olarak kayıt (her yerde aynı nesne kullanılsın)
container.register("logger", lambda: LoggerService(), singleton=True)
container.register("emailer", lambda: EmailService(), singleton=True)
container.register("payment", lambda: PaymentService(), singleton=True)

# FlightReservationService kayıt (diğerlerini resolve ederek)
container.register("reservation_service", lambda: FlightReservationService(
    container.resolve("logger"),
    container.resolve("emailer"),
    container.resolve("payment")
))

 Kullanım

reservation_service = container.resolve("reservation_service")
reservation_service.reserve("Merve Aydın", "IST456", 5500)

Test
def test_logger_singleton():
    logger1 = container.resolve("logger")
    logger2 = container.resolve("logger")
    assert logger1 is logger2

def test_reservation_service():
    service = container.resolve("reservation_service")
    service.reserve("Test Kullanıcı", "TEST001", 1000)
