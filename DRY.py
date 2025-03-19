"""DRY (Don't Repeat Yourself) Nedir?
DRY (Don't Repeat Yourself), yazılım geliştirme sürecinde kod tekrarını önlemek için kullanılan bir prensiptir. Tekrar eden kod bloklarını ortadan kaldırarak, daha temiz, bakımı kolay ve ölçeklenebilir kod yazmayı amaçlar.

🔹 DRY Prensibinin Faydaları
✔ Kod Tekrarını Azaltır → Aynı işlevi birden fazla yerde yazmak yerine, bir fonksiyon veya sınıf içinde tanımlayarak tekrar kullanım sağlar.
✔ Bakımı Kolaylaştırır → Kodda bir değişiklik yapmanız gerektiğinde, tek bir noktada güncelleme yapmanız yeterlidir.
✔ Hata Riskini Azaltır → Tekrarlanan kodlar, hata yapma ihtimalini artırır. DRY sayesinde kodu merkezi bir yerde yöneterek hataları azaltırsınız.
✔ Kodun Anlaşılabilirliğini Artırır → Daha modüler bir yapı oluşturulduğunda, kod okunabilir ve yönetilebilir hale gelir.

🔹 DRY Prensibine Aykırı Bir Örnek (Kötü Kod)
Aşağıdaki örnekte, aynı hesaplama işlemi iki farklı yerde tekrar edilmiştir.


def hesapla_maas1(saatlik_ucret, calisma_saati):
    maas = saatlik_ucret * calisma_saati
    vergi = maas * 0.2
    net_maas = maas - vergi
    return net_maas

def hesapla_maas2(saatlik_ucret, calisma_saati):
    maas = saatlik_ucret * calisma_saati
    vergi = maas * 0.2
    net_maas = maas - vergi
    return net_maas
🔴 Sorun: Aynı hesaplama iki farklı yerde tekrar edilmiş. Eğer hesaplama mantığında bir değişiklik yapılması gerekirse, iki fonksiyonun da güncellenmesi gerekecek.

🔹 DRY Prensibine Uygun Hali (İyi Kod)
Kod tekrarını önlemek için ortak bir fonksiyon oluşturabiliriz:


def hesapla_maas(saatlik_ucret, calisma_saati):
    maas = saatlik_ucret * calisma_saati
    return maas - maas * 0.2  # Vergiyi çıkardık

def calisan_bilgileri():
    return hesapla_maas(100, 40)  # Tek fonksiyon çağrılıyor

def yonetici_bilgileri():
    return hesapla_maas(200, 40)  # Aynı hesaplama farklı parametrelerle kullanılıyor
✅ Çözüm: Şimdi maaş hesaplaması tek bir fonksiyonda toplandı ve farklı yerlerde bu fonksiyon tekrar kullanıldı.

🔹 DRY Uygulama Yöntemleri
Fonksiyonlar Kullanarak Kod Tekrarını Önleme

Sık kullanılan işlemleri tek bir fonksiyonda toplamak.
Sınıflar ve Nesne Yönelimli Programlama (OOP)

Ortak özellikleri olan nesneleri sınıflar halinde düzenleyerek tekrarları azaltmak.
Modüler Programlama

Kod parçalarını farklı modüllere ayırarak düzen sağlamak.
Template Kullanımı (Web Geliştirme İçin)

HTML veya Frontend kodlarında tekrar eden bileşenler için template sistemleri kullanmak (örneğin, Django Templates, React Components).
🔹 DRY Prensibini İhlal Eden Durumlar (WET)
Eğer DRY uygulanmazsa, WET (Write Everything Twice) veya DAMP (Don't Abstract Meaninglessly) gibi kötü uygulamalar ortaya çıkar:
🔴 Kod tekrarına neden olur.
🔴 Bakımı zorlaştırır.
🔴 Hata oranını artırır.
Bir API geliştirirken, aynı kodu farklı endpoint’lerde kullanmak DRY prensibine aykırıdır.

Kötü Örnek (Kod Tekrarı İçeren API)
Aşağıda, hem get_user_by_id() hem de get_user_by_email() fonksiyonları benzer sorguları tekrar ediyor:


def get_user_by_id(user_id):
    user = db.session.query(User).filter(User.id == user_id).first()
    return user

def get_user_by_email(email):
    user = db.session.query(User).filter(User.email == email).first()
    return user
🔴 Sorun: Aynı sorgu mantığı iki yerde tekrar ediyor.

İyi Örnek (Tekrarı Azaltılmış API)
Bu fonksiyon, dinamik parametreler alarak hem ID hem de e-posta ile kullanıcı sorgulamayı sağlar:


def get_user(filter_by, value):
    return db.session.query(User).filter(getattr(User, filter_by) == value).first()
✔ Artık ID veya e-posta ile kullanıcı sorgulamak için tek bir fonksiyon kullanabiliriz:


user_by_id = get_user("id", 1)
user_by_email = get_user("email", "ahmet@abc.com")
✅ Çözüm: Kod tekrarını azalttık ve API'yi daha esnek hale getirdik.

3️⃣ DRY ve Frontend Geliştirme
Özellikle HTML, CSS ve JavaScript gibi teknolojilerde, bileşenleri tekrar kullanmak DRY prensibine uygun bir yaklaşımdır.

Kötü Örnek (Aynı HTML Kodunu Tekrar Kullanmak)
Eğer bir web sitesinde aynı buton farklı yerlerde kopyalanıyorsa, DRY prensibine aykırıdır:

html

<button class="btn">Kaydet</button>
<button class="btn">Sil</button>
<button class="btn">Güncelle</button>
🔴 Sorun: Eğer butonun stilini değiştirmek istersek, tüm butonları güncellemek zorunda kalırız.

İyi Örnek (Tekrarı Azaltılmış Frontend Bileşeni)
React veya Vue gibi modern framework'lerde bileşenler kullanarak tekrar eden kodları önleyebiliriz.

jsx
Kopyala
Düzenle
const Button = ({ text }) => {
  return <button className="btn">{text}</button>;
};

// Kullanım:
<Button text="Kaydet" />
<Button text="Sil" />
<Button text="Güncelle" />
✅ Çözüm: Buton bileşeni oluşturduk ve her yerde aynı kodu tekrar etmeden kullandık.

4️⃣ DRY ve Test Otomasyonu
Testlerde aynı kodları tekrar yazmak yerine, ortak helper fonksiyonlar kullanmalıyız.

Kötü Örnek (Aynı Test Adımları Tekrar Edilmiş)

def test_login_admin():
    driver.get("https://site.com/login")
    driver.find_element(By.NAME, "username").send_keys("admin")
    driver.find_element(By.NAME, "password").send_keys("1234")
    driver.find_element(By.NAME, "submit").click()

def test_login_user():
    driver.get("https://site.com/login")
    driver.find_element(By.NAME, "username").send_keys("user")
    driver.find_element(By.NAME, "password").send_keys("5678")
    driver.find_element(By.NAME, "submit").click()
🔴 Sorun: Giriş işlemi için aynı adımlar iki kez yazılmış.

İyi Örnek (Tekrarı Azaltılmış Test Fonksiyonu)

def login(username, password):
    driver.get("https://site.com/login")
    driver.find_element(By.NAME, "username").send_keys(username)
    driver.find_element(By.NAME, "password").send_keys(password)
    driver.find_element(By.NAME, "submit").click()

def test_login_admin():
    login("admin", "1234")

def test_login_user():
    login("user", "5678")
✅ Çözüm: login() fonksiyonunu yazarak kod tekrarını ortadan kaldırdık.

5️⃣ DRY ve Dökümantasyon
Sadece kod değil, dökümantasyon yazarken de tekrar eden ifadeleri ortadan kaldırmak önemlidir.

🔴 Kötü Örnek: Aynı API dökümantasyonu her endpoint için ayrı yazılmış.
✅ İyi Örnek: Swagger veya OpenAPI kullanarak dökümantasyonu otomatik oluşturmak.

Sonuç: DRY Kodu Daha İyi Hale Getirir
DRY prensibini uygulayarak: ✔ Daha temiz,
✔ Daha esnek,
✔ Daha bakımı kolay,
✔ Daha hata oranı düşük
yazılımlar geliştirebiliriz!"""

