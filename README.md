# PYTHON-202-BOOTCAMP-PROJECT
# Python ile Gelişmiş Kütüphane Yönetim Sistemi

Bu proje, Global AI Hub Python 202 Bootcamp kapsamında geliştirdiğim, Nesne Yönelimli Programlama (OOP), Harici API Kullanımı ve FastAPI ile kendi API'nizi oluşturma konularını birleştiren bir kütüphane yönetim sistemidir.

Projeyi, üç aşamada geliştirdim:
1.  **OOP ile Terminal Uygulaması:** Konsol üzerinden kitap ekleme, listeleme ve silme işlemleri.
2.  **Harici API Entegrasyonu:** Open Library API'den ISBN ile kitap bilgisi çekme.
3.  **FastAPI ile Web Servisi:** Kütüphane yönetimini HTTP API'leri aracılığıyla web üzerinden erişilebilir hale getirme.

## Kurulum

Projeyi yerel makinenizde çalıştırmak için aşağıdaki adımları takip edebilirsiniz.

1.  **Depoyu Klonlama:**
    ```bash
    git clone <depo-adresiniz>
    cd <proje-klasor-adiniz>
    ```

2.  **Bağımlılıkların Kurulması:**
    Gerekli tüm kütüphaneler (FastAPI, Uvicorn, Httpx vb.) `requirements.txt` dosyasında listelenmiştir. Bunları kurmak için aşağıdaki komutu çalıştırın:
    ```bash
    uv pip install -r requirements.txt
    ```

## Kullanım

### Aşama 1 ve 2: Terminal Uygulaması

Terminal uygulamasını başlatmak için aşağıdaki komutu kullanın:
```bash
python main.py
