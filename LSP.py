"""LSP — Liskov Substitution Principle
(Barbara Liskov tarafından 1987'de ortaya atılmıştır.)

📌 Tanım:
Bir alt sınıf, üst sınıfın yerine geçebilmeli ve programın doğru çalışmasını bozmamalıdır.

Yani:

"Alt sınıflar, base class’ların yerine sorunsuzca kullanılabilmelidir.**

📚 Türkçesiyle:
Eğer bir fonksiyon, bir üst sınıf (base class)
bekliyorsa, ona verdiğin alt sınıf (subclass) da aynı şekilde çalışmalı,
hatalara veya anlamsız davranışlara yol açmamalıdır.

🔎 Neden Önemli?
Eğer alt sınıf, üst sınıfın davranışını tam olarak desteklemiyorsa,
o zaman miras (inheritance) amacına ulaşmaz.

Kodun bakımını zorlaştırır, garip bug’lar, kırılan davranışlar oluşur.

❌ Kötü Örnek (LSP İhlali):
python
Kopyala
Düzenle
class Bird:
    def fly(self):
        print("Uçuyor")

class Ostrich(Bird):
    def fly(self):
        raise Exception("Devekuşu uçamaz!")

def make_it_fly(bird: Bird):
    bird.fly()

ostrich = Ostrich()
make_it_fly(ostrich)  # ❌ Exception fırlatır → LSP ihlali
Burada Ostrich, Bird’den türemiş ama onun yerine geçince beklenmedik bir hata veriyor. Bu, LSP’ye aykırıdır.

✅ İyi Örnek (LSP Uygun):
python
Kopyala
Düzenle
from abc import ABC, abstractmethod

class Bird(ABC):
    @abstractmethod
    def move(self):
        pass

class FlyingBird(Bird):
    def move(self):
        print("Uçarak hareket ediyor")

class WalkingBird(Bird):
    def move(self):
        print("Yürüyerek hareket ediyor")

def move_bird(bird: Bird):
    bird.move()

# Kullanım
move_bird(FlyingBird())   # ✅
move_bird(WalkingBird())  # ✅
Burada tüm alt sınıflar move() metodunu anlamlı bir şekilde override ediyor.
Hiçbir durumda program bozulmaz. LSP’ye uygun bir tasarım.

💡 Kısaca Akılda Kalması İçin:
"Bir sınıfın çocukları (subclass'ları), ebeveyni (base class) gibi davranmalı."
"Alt sınıf, üst sınıfın yerine geçmeli ve sistem normal çalışmalı."

📌 LSP ile İlgili İpuçları:
İstenmeyen override’lardan kaçın (örneğin bir metod alt sınıf için anlamsızsa, orada olmamalı).

Alt sınıf, üst sınıfın sözleşmesini bozmamalıdır (örneğin beklenmedik exception fırlatmamalı).

Eğer "bu alt sınıf burada çalışmaz" diyorsan, LSP ihlal ediliyor demektir.

Senaryo: Uçuş Rezervasyon Sistemi
Sistemimizde iki tür yolcu var:

Yetişkin (AdultPassenger)

Çocuk (ChildPassenger)

Yetişkinler bilet satın alabilir.
Çocuklar tek başına bilet alamaz, mutlaka bir veli gerekir.

Şimdi, kötü ve iyi tasarımları görelim.

❌ LSP’ye Aykırı (Kötü Örnek)
python
Kopyala
Düzenle
class Passenger:
    def buy_ticket(self):
        print("Bilet satın alındı.")

class ChildPassenger(Passenger):
    def buy_ticket(self):
        raise Exception("Çocuk yolcu kendi başına bilet alamaz!")

def purchase(p: Passenger):
    p.buy_ticket()

purchase(Passenger())       # ✅ Çalışır
purchase(ChildPassenger())  # ❌ Exception → LSP ihlali
Burada ChildPassenger, Passenger sınıfını türetmiş ama onun yerine geçtiğinde sistem bozuluyor.
Bu, Liskov Substitution Principle'a aykırıdır.

✅ LSP’ye Uygun (İyi Örnek)
python
Kopyala
Düzenle
from abc import ABC, abstractmethod

class Passenger(ABC):
    @abstractmethod
    def can_buy_ticket(self) -> bool:
        pass

class AdultPassenger(Passenger):
    def can_buy_ticket(self):
        return True

class ChildPassenger(Passenger):
    def can_buy_ticket(self):
        return False

def purchase(p: Passenger):
    if p.can_buy_ticket():
        print("Bilet satın alındı.")
    else:
        print("Bu yolcu tek başına bilet alamaz.")

# Kullanım
purchase(AdultPassenger())  # ✅ Bilet satın alındı
purchase(ChildPassenger())  # ✅ Uyarı verir ama sistem bozulmaz
Burada her iki sınıf da Passenger'ın yerine geçebiliyor.
Sistem bozulmuyor, exception fırlatmıyor, yani LSP’ye uygun.

🔁 Gerçek Hayatta LSP Neden Gerekli?
LSP’ye uymazsan:

Kodun tekrar tekrar test edilmek zorunda kalır

Alt sınıfların sisteme entegresi zorlaşır

“Polimorfizm” anlamını yitirir

👑 Sonuç

Tasarım	LSP'ye Uygun mu?	Açıklama
ChildPassenger.buy_ticket() exception fırlatıyor	❌ Hayır	Üst sınıf gibi davranamıyor
ChildPassenger.can_buy_ticket() false döndürüyor	✅ Evet	Üst sınıfın yerine geçip sistemi bozmuyor
"""