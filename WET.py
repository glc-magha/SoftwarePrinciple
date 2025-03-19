"""Yazılım bağlamında WET (Don't Write Everything Twice) prensibi, tekrar eden kod yazmaktan kaçınmayı ifade eder. Bu, DRY (Don't Repeat Yourself) prensibinin tersidir.

WET kodun anlamı:
Fazla tekrar eden kodlar içerir.
Bakımı zorlaşır.
Hata yapma olasılığını artırır.
Kod tekrar kullanılabilirlik açısından zayıftır.
Örnek (WET Kod)

def toplam1(a, b):
    return a + b

def toplam2(x, y):
    return x + y
Burada iki fonksiyon da aynı işlemi yapıyor, bu gereksiz bir tekrar.

Örnek (DRY Kod)

def toplam(a, b):
    return a + b
Bu şekilde kod DRY prensibine uygun hale gelmiş olur.

Genellikle WET kod, kötü yazılım geliştirme alışkanlıklarıyla ilişkilendirilir. Daha modüler, okunabilir ve sürdürülebilir kod yazmak için DRY, KISS (Keep It Simple, Stupid) ve SOLID gibi yazılım prensiplerine uymak önerilir.

WET Kodu Nasıl DRY Yapabiliriz?
Kod tekrarını azaltmak için şu teknikleri kullanabiliriz:

Fonksiyonlar ve Metotlar Kullanmak

Tekrar eden kod bloklarını fonksiyon veya metot haline getirerek ortak bir yapı oluşturabiliriz.
WET Örnek:


print("Merhaba, Ahmet!")
print("Merhaba, Mehmet!")
print("Merhaba, Ayşe!")
DRY Örnek:


def selam_ver(isim):
    print(f"Merhaba, {isim}!")

selam_ver("Ahmet")
selam_ver("Mehmet")
selam_ver("Ayşe")
Sınıflar ve Nesne Yönelimli Programlama (OOP) Kullanmak

Benzer özelliklere sahip nesneleri tek bir sınıf altında toplayarak tekrar eden kodları önleyebiliriz.
WET Örnek:


ahmet_ad = "Ahmet"
ahmet_yas = 25

mehmet_ad = "Mehmet"
mehmet_yas = 30
DRY Örnek (OOP ile):


class Kisi:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

ahmet = Kisi("Ahmet", 25)
mehmet = Kisi("Mehmet", 30)
Veri Yapıları Kullanmak

Tekrar eden değişkenleri listeler veya sözlükler gibi veri yapılarıyla düzenleyebiliriz.
WET Örnek:


ogrenci1 = "Ali"
ogrenci2 = "Veli"
ogrenci3 = "Ayşe"
DRY Örnek (Liste Kullanımı):


ogrenciler = ["Ali", "Veli", "Ayşe"]
Template Kullanımı (Özellikle Web Geliştirmede)

Web geliştirmede HTML şablonlarında ortak bileşenler kullanarak tekrar eden kodları azaltabiliriz.
WET Örnek (HTML Tekrarı):


<h1>Hoş Geldiniz</h1>
<p>Bu bir örnek sayfadır.</p>

<h1>İletişim</h1>
<p>Bize ulaşın!</p>
DRY Örnek (Template Kullanımı - Jinja2 Örneği):


{% for baslik, icerik in sayfalar %}
    <h1>{{ baslik }}</h1>
    <p>{{ icerik }}</p>
{% endfor %}
Sonuç
WET kod, yazılım geliştirme sürecini zorlaştırır, bakımı ve hata ayıklamayı güçleştirir.
DRY prensibi, tekrar eden kodları ortadan kaldırarak daha temiz, düzenli ve sürdürülebilir bir kod yapısı oluşturur.
Modüler programlama, fonksiyonlar, sınıflar ve veri yapıları kullanarak kod tekrarından kaçınabiliriz.

 WET Nedir? (Write Everything Twice)
WET kod, fazla tekrar eden ve optimize edilmemiş kodlar anlamına gelir. Bu tür kodlar genellikle hızla geliştirilmiş, ancak uzun vadede bakımı zor olan kodlardır.

WET Kodun Dezavantajları
Kod Tekrarı: Aynı kodu birçok kez yazmak, geliştirme sürecini yavaşlatır.
Bakım Zorluğu: Bir kod parçasında hata olduğunda, her yerde düzeltme yapmak gerekir.
Zaman Kaybı: Aynı işlevi yerine getiren kod bloklarının tekrar yazılması zaman kaybına neden olur.
Okunabilirlik Sorunu: Fazla tekrar, kodun okunmasını ve anlaşılmasını zorlaştırır.
WET Koda Örnek
Diyelim ki bir web sitesinde kullanıcıları karşılayan bir mesaj fonksiyonumuz var. Ancak bu fonksiyon tekrar tekrar yazılmış:


def selamla_ahmet():
    print("Merhaba, Ahmet!")

def selamla_mehmet():
    print("Merhaba, Mehmet!")

def selamla_ayse():
    print("Merhaba, Ayşe!")
Bu kod gereksiz yere tekrar içeriyor. Aynı işlemi yapan üç farklı fonksiyon yazmak yerine bir tane dinamik fonksiyon kullanmalıyız.

2. DRY Nedir? (Don't Repeat Yourself)
DRY prensibi, kod tekrarını önleyerek daha modüler, okunaklı ve ölçeklenebilir bir yapı oluşturmayı hedefler. DRY kodlar genellikle şu tekniklerle sağlanır:

Fonksiyonlar ve Metotlar
Döngüler ve Veri Yapıları
Nesne Yönelimli Programlama (OOP)
Şablon (Template) Kullanımı
Modüler Kodlama (Kütüphaneler, Modüller ve Paketler)
DRY Koda Örnek: Fonksiyon Kullanımı
WET koddaki tekrarları kaldırıp, bir fonksiyon kullanarak kodu optimize edelim:


def selamla(isim):
    print(f"Merhaba, {isim}!")

selamla("Ahmet")
selamla("Mehmet")
selamla("Ayşe")
Bu şekilde kod tekrarını ortadan kaldırmış olduk. Tek bir fonksiyon ile her ismi selamlayabiliriz.

3. DRY Prensibini Kullanarak WET Kodları Optimize Etme Yöntemleri
Kod tekrarını azaltmanın birçok yolu vardır. İşte en yaygın kullanılan yöntemler:

A) Fonksiyonlar ve Metotlar Kullanarak DRY Yapı Sağlamak
Tekrar eden kodları fonksiyonlar veya metotlar içinde toplamak, kodun daha düzenli olmasını sağlar.

WET Örnek

print("Kullanıcı adı: Ahmet")
print("Yaş: 25")
print("Kullanıcı adı: Mehmet")
print("Yaş: 30")
print("Kullanıcı adı: Ayşe")
print("Yaş: 22")
DRY Çözüm (Fonksiyon Kullanımı)

def kullanici_bilgileri(ad, yas):
    print(f"Kullanıcı adı: {ad}")
    print(f"Yaş: {yas}")

kullanici_bilgileri("Ahmet", 25)
kullanici_bilgileri("Mehmet", 30)
kullanici_bilgileri("Ayşe", 22)
Bu yöntemle kod tekrarını engelleyip, modüler hale getirmiş olduk.

B) Döngüler Kullanarak DRY Yapı Sağlamak
Tekrar eden ifadeleri döngülerle tek bir yerde toplamak mümkündür.

WET Örnek (Aynı Mesajı Tekrar Yazmak)

print("Merhaba Ahmet")
print("Merhaba Mehmet")
print("Merhaba Ayşe")
print("Merhaba Fatma")
DRY Çözüm (Döngü Kullanımı)

isimler = ["Ahmet", "Mehmet", "Ayşe", "Fatma"]

for isim in isimler:
    print(f"Merhaba {isim}")
Bu yöntemle hem kod tekrarını önledik hem de listeyi büyütebilir hale getirdik.

C) Nesne Yönelimli Programlama (OOP) Kullanarak DRY Yapı Sağlamak
Eğer birçok nesne ile çalışıyorsanız, sınıflar ve nesneler kullanarak kod tekrarını önleyebilirsiniz.

WET Örnek (Her Kullanıcı İçin Ayrı Değişken Tanımlamak)

ahmet_ad = "Ahmet"
ahmet_yas = 25

mehmet_ad = "Mehmet"
mehmet_yas = 30

ayse_ad = "Ayşe"
ayse_yas = 22
DRY Çözüm (OOP Kullanımı)

class Kullanici:
    def __init__(self, ad, yas):
        self.ad = ad
        self.yas = yas

k1 = Kullanici("Ahmet", 25)
k2 = Kullanici("Mehmet", 30)
k3 = Kullanici("Ayşe", 22)
Bu yöntem, kullanıcı verilerini tek bir sınıf altında toplar ve kod tekrarını büyük ölçüde azaltır.

D) Şablon Kullanımı ile DRY Yapı Sağlamak (Özellikle Web Geliştirmede)
Web geliştirmede, HTML sayfalarını şablonlarla yöneterek tekrar eden kodları azaltabiliriz.

WET Örnek (Her Sayfa İçin Aynı Yapıyı Tekrar Yazmak)

<h1>Hoş Geldiniz</h1>
<p>Bu bir test sayfasıdır.</p>

<h1>Hakkımızda</h1>
<p>Biz bir yazılım şirketiyiz.</p>

<h1>İletişim</h1>
<p>Bize ulaşabilirsiniz.</p>
DRY Çözüm (Template Kullanımı - Jinja2 Örneği)

{% for sayfa in sayfalar %}
    <h1>{{ sayfa.baslik }}</h1>
    <p>{{ sayfa.icerik }}</p>
{% endfor %}
Bu sayede yeni bir sayfa eklemek için sadece veri eklemek yeterli olacak, HTML dosyasını değiştirmeye gerek kalmayacak.

Sonuç ve Özet
WET (Write Everything Twice) prensibi, kod tekrarına neden olarak bakımı zor, hataya açık ve zaman kaybettiren bir yapı oluşturur.
DRY (Don't Repeat Yourself) prensibi, tekrarları ortadan kaldırarak daha düzenli, okunabilir ve sürdürülebilir bir kod yazmayı hedefler.
Fonksiyonlar, döngüler, OOP, şablonlar ve modüler programlama gibi tekniklerle kod tekrarını azaltabiliriz.
DRY prensibi, yazılım geliştirme sürecini hızlandırır ve hata oranını düşürür."""