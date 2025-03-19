"""SRP (Single Responsibility Principle) – Tek Sorumluluk İlkesi Nedir?
SRP (Single Responsibility Principle), SOLID prensiplerinin ilkidir ve yazılım geliştirmede her sınıfın yalnızca tek bir sorumluluğu olması gerektiğini belirtir.

Temel Mantık:
✔ Bir sınıfın veya fonksiyonun yalnızca tek bir amacı olmalıdır.
✔ Birden fazla sorumluluğu olan sınıflar, değişime daha duyarlı olur ve yönetilmesi zorlaşır.
✔ SRP'ye uymayan kod, bakım maliyetini artırır ve hata yapma olasılığını yükseltir.

🔹 SRP'yi İhlal Eden Bir Örnek (Kötü Kod)
Aşağıdaki User sınıfı, hem kullanıcı yönetimi hem de dosya kaydetme işlemlerini içeriyor.


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

    def save_to_file(self):
        with open("user_data.txt", "w") as file:
            file.write(f"Name: {self.name}, Email: {self.email}")
🔴 Sorun:

User sınıfı, hem kullanıcı bilgilerini tutuyor (veri modeli) hem de dosya kaydetme işlemi yapıyor (veri saklama işlemi).
Eğer dosya kaydetme işlemini değiştirmek istersek, kullanıcı yönetimi kodunu da değiştirmek zorundayız.
🔹 SRP'ye Uygun Hali (İyi Kod)
Sınıfların tek bir sorumluluğu olması gerektiği için, veri yönetimi ile veri kaydetme işlemlerini ayıralım.


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email

class UserRepository:
    @staticmethod
    def save_to_file(user: User):
        with open("user_data.txt", "w") as file:
            file.write(f"Name: {user.name}, Email: {user.email}")
✅ Çözüm:

User sınıfı sadece kullanıcı bilgilerini içeriyor.
UserRepository sınıfı, veri kaydetme işlemlerini yönetiyor.
Artık farklı bir veri saklama yöntemi kullanmak istersek, User sınıfını değiştirmeden sadece UserRepository'yi güncelleyebiliriz.

🔹 Gerçek Dünya Örneği: SRP'nin Önemi
Bir e-ticaret sisteminde Sipariş Yönetimi (Order Management) için bir sınıf oluşturduğumuzu düşünelim.

SRP'ye Aykırı Kötü Örnek

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def send_order_confirmation(self):
        print(f"Order {self.order_id} confirmed! Email sent to customer.")

    def save_order_to_db(self):
        print(f"Order {self.order_id} saved to database.")
🔴 Sorun:

Order sınıfı, sipariş yönetimi, toplam hesaplama, e-posta gönderme ve veritabanı işlemleri gibi birden fazla sorumluluğa sahip.
Eğer e-posta gönderme yöntemini değiştirirsek, sipariş yönetimi kodu da etkilenir.
SRP'ye Uygun İyi Örnek
Kodumuzu ayrı sorumluluklara bölerek daha esnek ve sürdürülebilir hale getirebiliriz.


class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

class OrderCalculator:
    @staticmethod
    def calculate_total(order: Order):
        return sum(item["price"] for item in order.items)

class OrderNotifier:
    @staticmethod
    def send_order_confirmation(order: Order):
        print(f"Order {order.order_id} confirmed! Email sent to customer.")

class OrderRepository:
    @staticmethod
    def save_order_to_db(order: Order):
        print(f"Order {order.order_id} saved to database.")
✅ Çözüm:

Order → Sadece sipariş bilgilerini içerir.
OrderCalculator → Sipariş toplamını hesaplar.
OrderNotifier → Sipariş onay e-postası gönderir.
OrderRepository → Veritabanı işlemlerini yönetir.
Bu yapı sayesinde her bir sınıfın sorumluluğu tek bir şeye odaklanmıştır.

🔹 SRP'nin Avantajları
✔ Bakımı Kolaylaştırır → Bir sınıfta değişiklik yaparken diğer bölümleri etkilemez.
✔ Kod Tekrarını Önler → Aynı işlev için tekrar tekrar kod yazmaya gerek kalmaz.
✔ Test Edilebilirliği Artırır → Küçük ve bağımsız sınıflar, daha kolay test edilir.
✔ Esnekliği Artırır → Yeni özellik eklemek veya değiştirmek daha kolay olur.

🔹 SRP'nin Gerçek Hayatta Kullanımı
✅ Django ve Flask gibi framework'lerde Model, View ve Controller (MVC) yapıları SRP'ye uygundur.
✅ React ve Vue gibi frontend framework'lerinde bileşen tabanlı yapı SRP’yi destekler.
✅ Microservice mimarisi, sistem bileşenlerini tek bir sorumluluğa sahip olacak şekilde tasarlar.

🔹 Sonuç: SRP Olmadan Ne Olur?
🔴 Kod karmaşıklaşır ve yönetimi zorlaşır.
🔴 Basit bir değişiklik, birçok yeri etkileyebilir.
🔴 Test etmek zorlaşır.
🔴 Yazılım büyüdükçe hata oranı artar.

SRP (Single Responsibility Principle) – Derinlemesine Analiz
SRP (Tek Sorumluluk İlkesi), yazılımın uzun vadede sürdürülebilir, test edilebilir ve kolay geliştirilebilir olmasını sağlamak için kritik bir ilkedir.

Bu bölümü biraz daha derinlemesine inceleyelim:

📌 1. SRP'nin Gerçek Hayattaki Mantığı
SRP'yi gerçek hayattan bir örnekle düşünelim:

Bir araba düşünelim. Arabanın motoru, tekerlekleri, frenleri ve radyo sistemi farklıdır. Motorun görevi hareket sağlamak, frenlerin görevi durdurmak, radyonun görevi ise müzik çalmaktır.

Eğer motor aynı zamanda müzik çalmaktan da sorumlu olsaydı, sistemi değiştirmek çok zor olurdu. Radyo bozulduğunda motorun da çalışmama ihtimali doğardı!

Yazılımda da aynı mantık geçerlidir! Bir sınıfın veya modülün yalnızca tek bir görevi olmalıdır.

📌 2. SRP'yi Bozan En Yaygın Hatalar
Bir sınıfın birden fazla sorumluluğa sahip olması yazılımın bakımını zorlaştırır. İşte bazı yaygın SRP ihlalleri:

🔴 1️⃣ Bir sınıfın hem veri yönetimi hem de iş mantığını içermesi
🔴 2️⃣ Aynı sınıfın hem veritabanı işlemlerini hem de e-posta gönderimini yapması
🔴 3️⃣ Tek bir fonksiyonun birden fazla işlem yapması (Örneğin: Veritabanına kayıt yapıp, bir dosyaya da log yazması)
🔴 4️⃣ Farklı işlemler için ortak olan ancak birbiriyle ilgisi olmayan metotların tek bir sınıfta bulunması

📌 3. SRP'nin Yanlış Anlaşılması
Bazı yazılımcılar SRP'yi fazla abartarak kodu gereksiz yere parçalara bölebilir. SRP, "her fonksiyon sadece bir satır içermeli" anlamına gelmez!

🔹 SRP'nin amacı, bir sınıfın tek bir "sebebe" bağlı olarak değişebilmesini sağlamaktır.
🔹 Kodun okunabilirliğini düşürmeden, yalnızca gerçekten farklı sorumlulukları ayırmalıyız.

Örneğin, aşağıdaki gibi aşırı bölünmüş kod gereksizdir:


class ReadData:
    def read(self, source):
        return source.get_data()

class ProcessData:
    def process(self, data):
        return [x * 2 for x in data]

class SaveData:
    def save(self, data, destination):
        destination.save_data(data)
Bu kod gereğinden fazla bölünmüştür ve küçük işlemleri yönetmeyi zorlaştırabilir.

✔ Doğru SRP uygulaması, mantıklı şekilde bölünmüş sorumluluklar içermelidir.

📌 4. SRP'nin Büyük Projelerde Kullanımı
Büyük projelerde SRP kodu modüler hale getirerek geliştirmeyi kolaylaştırır.

Örneğin bir e-ticaret uygulamasında SRP'yi şu şekilde uygulayabiliriz:

Kötü Örnek: SRP'yi İhlal Eden Kod

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

    def calculate_total(self):
        return sum(item["price"] for item in self.items)

    def send_invoice(self):
        print(f"Fatura gönderildi: {self.order_id}")

    def save_to_db(self):
        print(f"Sipariş kaydedildi: {self.order_id}")
🔴 Sorun:

Order sınıfı hem sipariş işlemlerini, hem toplam hesaplamayı, hem fatura işlemlerini hem de veritabanı işlemlerini yapıyor.
Eğer fatura gönderme işlemi değişirse, tüm Order sınıfı etkilenir.
İyi Örnek: SRP'yi Uygulayan Kod

class Order:
    def __init__(self, order_id, items):
        self.order_id = order_id
        self.items = items

class OrderCalculator:
    @staticmethod
    def calculate_total(order: Order):
        return sum(item["price"] for item in order.items)

class InvoiceService:
    @staticmethod
    def send_invoice(order: Order):
        print(f"Fatura gönderildi: {order.order_id}")

class OrderRepository:
    @staticmethod
    def save_to_db(order: Order):
        print(f"Sipariş kaydedildi: {order.order_id}")
✅ Çözüm:

Order yalnızca sipariş bilgilerini içerir.
OrderCalculator sipariş tutarını hesaplar.
InvoiceService fatura işlemlerini yönetir.
OrderRepository siparişi veritabanına kaydeder.
Bu şekilde her sınıfın tek bir sorumluluğu var ve değişiklik yaparken sadece ilgili sınıfı düzenlememiz yeterli oluyor!

📌 5. SRP'nin Avantajları
✅ 1️⃣ Daha Kolay Bakım → Eğer bir özellik değiştirilirse, diğer kodlar etkilenmez.
✅ 2️⃣ Daha Kolay Test Edilebilirlik → Her sınıf bağımsız olduğu için birim testler daha kolay yazılır.
✅ 3️⃣ Daha Kolay Genişletilebilirlik → Yeni özellik eklemek daha kolay olur.
✅ 4️⃣ Daha Az Hata → Bir sınıfın çok fazla işi olmadığından hata yapma ihtimali azalır.
✅ 5️⃣ Daha Anlaşılır Kod → Kod daha düzenli ve anlaşılır hale gelir.

📌 6. SRP'nin Diğer SOLID Prensipleri ile İlişkisi
SRP, diğer SOLID prensipleriyle de bağlantılıdır:

✔ Open-Closed Principle (OCP) → Yeni özellik eklerken mevcut kodu değiştirmeden geliştirme yapmamıza yardımcı olur.
✔ Liskov Substitution Principle (LSP) → Bir sınıfın yerine başka bir sınıf koyduğumuzda sistemin bozulmamasını sağlar.
✔ Interface Segregation Principle (ISP) → Kullanılmayan metotları ayırarak SRP'nin güçlenmesini sağlar.
✔ Dependency Inversion Principle (DIP) → Kodun esnek ve bağımlılıklardan uzak olmasını sağlar.

📌 7. Sonuç: SRP Kullanmazsak Ne Olur?
🔴 Eğer SRP'yi ihmal edersek:

Kod çok karmaşık hale gelir
Küçük değişiklikler bile büyük problemlere neden olur
Test yazmak zorlaşır
Hata yapma ihtimali artar
Yazılım büyüdükçe yönetilemez hale gelir
✅ Eğer SRP'yi uygularsak:

Kod daha temiz, düzenli ve sürdürülebilir olur.
Değişiklikler daha kolay ve güvenli yapılır.
Ekip içi iş bölümü daha iyi yönetilir."""