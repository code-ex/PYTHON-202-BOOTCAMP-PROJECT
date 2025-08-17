# PYTHON-202-BOOTCAMP-PROJECT
Python ile Gelişmiş Kütüphane Yönetim Sistemi
Bu proje, Global AI Hub Python 202 Bootcamp kapsamında geliştirdiğim, Nesne Yönelimli Programlama (OOP), Harici API Kullanımı ve FastAPI ile kendi API'nizi oluşturma konularını birleştiren bir kütüphane yönetim sistemidir.

Proje, üç aşamada geliştirilmiştir:

1. OOP ile Terminal Uygulaması: Konsol üzerinden kitap ekleme, listeleme ve silme işlemleri.

2. Harici API Entegrasyonu: Open Library API'den ISBN ile kitap bilgisi çekme.

3. FastAPI ile Web Servisi: Kütüphane yönetimini HTTP API'leri aracılığıyla web üzerinden erişilebilir hale getirme.

Kurulum
Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

1. Depoyu Klonlama:
git clone <depo-adresiniz>
cd <proje-klasor-adiniz>

2. Bağımlılıkların Kurulması:
Gerekli tüm kütüphaneler (FastAPI, Uvicorn, Httpx vb.) requirements.txt dosyasında listelenmiştir. Bunları kurmak için aşağıdaki komutu çalıştırın:
uv pip install -r requirements.txt

Kullanım
Aşama 1 ve 2: Terminal Uygulaması
Terminal uygulamasını başlatmak için aşağıdaki komutu kullanın:
python main.py

Bu komutu çalıştırdığınızda, konsol üzerinden interaktif bir menü ile karşılaşacaksınız.

Aşama 3: API Sunucusu
FastAPI sunucusunu başlatmak için aşağıdaki komutu kullanın:
uvicorn api:app --reload

Sunucu başladığında, API'ye http://127.0.0.1:8000 adresinden erişebilirsiniz.

API Dokümantasyonu
API'nin tüm uç noktalarını (endpoints) ve interaktif dokümantasyonunu görmek için sunucu çalışırken aşağıdaki adresi ziyaret edebilirsiniz:
http://127.0.0.1:8000/docs

Aşağıda, oluşturulan ana uç noktaların bir listesi yer almaktadır:

HTTP Metodu | Uç Nokta | Açıklama
GET | /books | Kütüphanedeki tüm kitapları listeler.
GET | /books/{isbn} | Belirtilen ISBN'e sahip kitabı getirir.
POST | /books | Yeni bir kitabı manuel olarak ekler.
POST | /books/from-api/{isbn} | Harici API'den ISBN'ine göre kitap ekler.
PUT | /books/{isbn} | Belirtilen ISBN'e sahip kitabın bilgilerini günceller.
DELETE | /books/{isbn} | Belirtilen ISBN'e sahip kitabı siler.

Örnek POST İstek Gövdesi (Body):
/books uç noktasına POST isteği gönderirken kullanabileceğiniz JSON yapısı:

{
"eserAdı": "Simyacı",
"yazar": "Paulo Coelho",
"yayınTarihi": "1988",
"isbn": "978-975-07-0130-3"
}

Ek Bilgiler
Bu proje, Nesne Yönelimli Programlama (OOP) prensiplerini kullanarak modüler bir yapıya sahiptir.
Kitap verileri, library.json dosyasında kalıcı olarak saklanır.
API entegrasyonu için Open Library API kullanılmıştır.
