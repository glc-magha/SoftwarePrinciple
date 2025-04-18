"""DI — Dependency Injection (Bağımlılıkların Enjekte Edilmesi)
📌 Tanım:
Bir sınıfın ihtiyaç duyduğu (bağımlı olduğu) nesnelerin, kendisi tarafından oluşturulmak yerine dışarıdan verilmesidir.

🎯 Amaç:
Sınıflar birbirine sıkı sıkıya bağlı olmasın

Daha test edilebilir, esnek, bakımı kolay kod yazılsın

🧠 Temel Mantık:
Normalde bir sınıf ihtiyacı olan başka bir sınıfı kendi içinde oluşturur.
DI kullanıldığında bu sınıfı dışarıdan alır.

🔧 Basit Örnek
❌ Kötü Tasarım (Bağımlılığı içeride oluşturuyor)
python
Kopyala
Düzenle
class EmailService:
    def send_email(self, message):
        print("E-posta gönderildi:", message)

class UserService:
    def __init__(self):
        self.email_service = EmailService()  # ❌ Bağımlılığı içeride oluşturuyor

    def register_user(self):
        print("Kullanıcı kaydedildi.")
        self.email_service.send_email("Hoş geldiniz!")
Bu tasarımda UserService, EmailService'e sıkı bağlı (tight coupling).
Test etmek veya SMSService ile değiştirmek zordur.

✅ İyi Tasarım (Dependency Injection ile)
python
Kopyala
Düzenle
class EmailService:
    def send_email(self, message):
        print("E-posta gönderildi:", message)

class UserService:
    def __init__(self, email_service: EmailService):
        self.email_service = email_service  # ✅ Bağımlılığı dışarıdan alıyor

    def register_user(self):
        print("Kullanıcı kaydedildi.")
        self.email_service.send_email("Hoş geldiniz!")
Kullanım:

python
Kopyala
Düzenle
email_service = EmailService()
user_service = UserService(email_service)
user_service.register_user()
Bu şekilde:

UserService artık EmailService’i kendisi oluşturmaz.

Daha kolay test edilir (Mock objeler verilebilir).

Farklı tür servislerle (örneğin SMSService) değiştirmek kolaydır.

🔄 DI Nasıl Uygulanır?

Tür	Açıklama
Constructor Injection	Gerekli bağımlılıklar yapıcı metod (__init__) ile verilir.
(En yaygın yöntem)
Setter Injection	Bağımlılıklar bir ayarlayıcı (setter) metodla sonradan verilir.
Interface Injection	Sınıfın kendisi bir bağımlılığı alabilmek için bir interface (arayüz) uygular. (Java/C# gibi dillerde)
💼 Gerçek Hayat Uygulaması: (Flight App üzerinden)
Bir PaymentService, farklı ödeme yöntemlerine ihtiyaç duyabilir:

Kredi Kartı

Banka Transferi

Sanal Cüzdan

❌ Kötü Yaklaşım:
python
Kopyala
Düzenle
class PaymentService:
    def __init__(self):
        self.method = CreditCardPayment()  # Sıkı bağlı
✅ DI ile:
python
Kopyala
Düzenle
class PaymentService:
    def __init__(self, payment_method):
        self.method = payment_method  # Dışarıdan alır

    def pay(self, amount):
        self.method.process(amount)
✅ DI’nin Avantajları:
Modülerlik

Test edilebilirlik (Mock ile kolay test)

Bağımlılık yönetimi kolaylaşır

Farklı servislerle çalışmak kolay olur

🤖 Bonus: DI Frameworkleri (Gelişmiş kullanım için)
Bazı dillerde DI otomatik yapılır:

Spring (Java)

.NET Core (C#)

Angular (TypeScript)

Python'da: dependency-injector, injector gibi kütüphaneler
Senaryo: Flight Reservation Sistemi
🧩 Bileşenler:
FlightReservationService: Uçuş rezervasyonu yapar.

LoggerService: Log işlemlerini yapar (konsola veya dosyaya).

DI ile: LoggerService, FlightReservationService’e dışarıdan enjekte edilir.

🔧 1. Önce Bağımlılığı Tanımlayalım (LoggerService)

class LoggerService:
    def log(self, message: str):
        print("[LOG]:", message)
🔧 2. FlightReservationService (DI ile)

class FlightReservationService:
    def __init__(self, logger: LoggerService):
        self.logger = logger

    def reserve_flight(self, passenger_name: str, flight_no: str):
        # Rezervasyon işlemleri...
        self.logger.log(f"{passenger_name} için {flight_no} numaralı uçuş rezerve edildi.")
        print("Rezervasyon başarılı!")
✅ 3. Kullanım (Bağımlılığı dışarıdan veriyoruz)

logger = LoggerService()
reservation_service = FlightReservationService(logger)

reservation_service.reserve_flight("Ahmet Yılmaz", "IST123")
📤 Çıktı:


[LOG]: Ahmet Yılmaz için IST123 numaralı uçuş rezerve edildi.
Rezervasyon başarılı!
🔄 Alternatif Logger Ekleyelim

class FileLoggerService(LoggerService):
    def log(self, message: str):
        with open("log.txt", "a") as f:
            f.write("[FILE LOG]: " + message + "\n")
Kullanım:


file_logger = FileLoggerService()
reservation_service = FlightReservationService(file_logger)

reservation_service.reserve_flight("Zeynep Kaya", "ANK456")
✔️ Hiçbir sınıfı değiştirmedik! Sadece yeni bir logger vererek sistemi değiştirdik.
İşte Dependency Injection’ın gücü burada!

🧪 Test Edilebilirlik İçin (Mock Logger)

class MockLogger(LoggerService):
    def __init__(self):
        self.logs = []

    def log(self, message: str):
        self.logs.append(message)

# Test
mock_logger = MockLogger()
service = FlightReservationService(mock_logger)
service.reserve_flight("Test Kullanıcı", "TEST001")

assert "Test Kullanıcı için TEST001 numaralı uçuş rezerve edildi." in mock_logger.logs
🎁 Daha Gelişmiş: Birden Fazla Bağımlılık
python
Kopyala
Düzenle
class EmailService:
    def send_confirmation(self, passenger_name):
        print(f"{passenger_name} adlı yolcuya onay e-postası gönderildi.")

class FlightReservationService:
    def __init__(self, logger: LoggerService, emailer: EmailService):
        self.logger = logger
        self.emailer = emailer

    def reserve_flight(self, passenger_name: str, flight_no: str):
        self.logger.log(f"{passenger_name} için {flight_no} numaralı uçuş rezerve edildi.")
        self.emailer.send_confirmation(passenger_name)
Kullanım:

logger = LoggerService()
emailer = EmailService()
reservation_service = FlightReservationService(logger, emailer)

reservation_service.reserve_flight("Burak Demir", "IZM789")
🎯 Özet:

Özellik	Açıklama
🔁 Esneklik	Logger’ı, Emailer’ı değiştirmek için FlightReservationService'i değiştirmeye gerek yok
🧪 Test Edilebilirlik	Mock servisler ile kolay test
🔧 Bakım Kolaylığı	Her sınıf kendi işini yapar, bağımlılıklar dışarıdan verilir
♻️ Bağımlılık Yönetimi	Modüler yapı, yeniden kullanılabilir bileşenler"""