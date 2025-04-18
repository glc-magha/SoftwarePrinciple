""" Open/Closed Principle (Açık/Kapalı Prensibi)
Nesne yönelimli programlamada (OOP) kullanılan SOLID prensiplerinden biridir.
 OCP şu şekilde tanımlanır:

("Bir yazılım bileşeni (sınıf, modül, fonksiyon vs.), genişletilmeye açık,"
 " fakat değiştirmeye kapalı olmalıdır.")

Anlamı:
Mevcut kodu değiştirmeden, yeni özellikler ekleyebilmelisin.

Yani, sistemi bozmadan geliştirebilir olmalısın.

Örnek:
Kötü örnek:


class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Daire çiz")

class Rectangle(Shape):
    def draw(self):
        print("Dikdörtgen çiz")

# Bu sınıf OCP'yi ihlal ediyor çünkü her yeni şekil için kodu değiştirmemiz gerekiyor.
class DrawingTool:
    def draw_shape(self, shape):
        shape.draw()
İyi örnek (OCP’ye uygun):


class Shape:
    def draw(self):
        pass

class Circle(Shape):
    def draw(self):
        print("Daire çiz")

class Triangle(Shape):
    def draw(self):
        print("Üçgen çiz")

# Yeni şekiller eklerken mevcut kodu değiştirmemize gerek yok.
def render(shape: Shape):
    shape.draw()
2. Oracle Certified Professional (OCP)
Eğer yazılım geliştirici değil de sertifikasyon dünyasında duydunsa, OCP şu anlama gelir:

Oracle Certified Professional
Oracle tarafından verilen, Java, veritabanı yönetimi, yazılım geliştirme gibi konularda uzmanlık belgesidir.

Örneğin:
OCP Java SE 11 Developer

OCP Oracle Database Administrator

 Open/Closed Principle (Açık/Kapalı Prensibi)
📌 Tanım:
Bir yazılım bileşeni "geliştirmeye açık" ama "değişikliğe kapalı" olmalıdır.
Bu, mevcut kodu bozmadan yeni işlevsellik ekleyebilmek anlamına gelir.

🧠 Mantığı:
Kodun bir kez yazıldıktan sonra mümkün olduğunca dokunulmadan kalması gerekir. Çünkü değişiklik:

Yeni hatalar doğurabilir

Mevcut işleyişi bozabilir

Testleri boşa çıkarabilir

Bu yüzden kodun esnek olması gerekir:
Yeni ihtiyaçlara kod ekleyerek (extend) cevap ver, kod değiştirerek (modify) değil!

📊 Uygulama Yolları:
Soyutlamalar (abstract class / interface) kullanılır.

Alt sınıflar üzerinden sistem genişletilir.

Polimorfizm ile davranışlar değiştirilir.

✅ OCP’ye Uygun Örnek (Python):

from abc import ABC, abstractmethod

class Notification(ABC):
    @abstractmethod
    def send(self, message):
        pass

class EmailNotification(Notification):
    def send(self, message):
        print("Email gönderildi:", message)

class SMSNotification(Notification):
    def send(self, message):
        print("SMS gönderildi:", message)

def notify_users(notifier: Notification, message):
    notifier.send(message)

# Kullanım
email = EmailNotification()
sms = SMSNotification()

notify_users(email, "Merhaba!")
notify_users(sms, "Selam!")
Bu sistemde yeni bir PushNotification sınıfı eklemek için sadece yeni bir sınıf yazılır, mevcut kod satırlarına dokunulmaz.

❌ OCP’ye Aykırı Örnek:
python
Kopyala
Düzenle
def notify_users(type, message):
    if type == "email":
        print("Email gönderildi:", message)
    elif type == "sms":
        print("SMS gönderildi:", message)
Burada yeni bir tür eklemek için fonksiyonu değiştirmen gerekir → OCP ihlali!

🔹 2. Oracle Certified Professional (Sertifika Olarak OCP)
🎓 Nedir?
Oracle tarafından verilen ve dünya genelinde tanınan resmi bir sertifikadır. Genellikle şu alanları kapsar:

Java (en yaygın olanı)

Oracle Database

Oracle Cloud

SQL, PL/SQL

System/DB Admin



"""