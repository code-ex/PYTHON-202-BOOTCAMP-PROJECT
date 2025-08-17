import json
import os
import httpx
from book import Book  # book.py dosyasındaki Book sınıfını içe aktarıyoruz

class Library:
    def __init__(self, json_file='library.json'):
        self.json_file = json_file
        self.books = []
        self.load_books()

    def load_books(self):
        if os.path.exists(self.json_file):
            with open(self.json_file, 'r') as f:
                books_data = json.load(f)
                self.books = [Book(book_data['eserAdı'], book_data['yazar'], book_data['yayınTarihi'], book_data['isbn']) for book_data in books_data]
        else:
            self.books = []

    def save_books(self):
        with open(self.json_file, 'w') as f:
            books_to_save = [book.__dict__ for book in self.books]
            json.dump(books_to_save, f, indent=4)

    def add_book(self, book):
        self.books.append(book)
        self.save_books()
        print(f"Kitap eklendi: {book}")

    def list_books(self):
        if not self.books:
            print("Kütüphanede henüz hiç kitap yok.")
        else:
            print("\n--- Kütüphanedeki Kitaplar ---")
            for book in self.books:
                print(book)
            print("----------------------------\n")

    def remove_book(self, isbn):
        book_to_remove = self.find_book(isbn)
        if book_to_remove:
            self.books.remove(book_to_remove)
            self.save_books()
            print(f"'{book_to_remove.eserAdı}' başarıyla silindi.")
            return True
        else:
            print("Belirtilen ISBN'de kitap bulunamadı.")
            return False

    def find_book(self, isbn):
        for book in self.books:
            if book.isbn == isbn:
                return book
        return None
    
    # Gelişmiş arama sekmesi eklemek istedim.
    def find_by_author(self, yazar_adı):
        # Yazar adına göre kitapları bulur
        found_books = [book for book in self.books if book.yazar.lower() == yazar_adı.lower()]
        if not found_books:
            print(f"'{yazar_adı}' yazarına ait kitap bulunamadı.")
        else:
            print(f"\n--- '{yazar_adı}' Yazarına Ait Kitaplar ---")
            for book in found_books:
                print(book)
            print("------------------------------------------\n")

    def find_by_publication_year(self, yıl):
        # Yayın yılına göre kitapları bulur
        found_books = [book for book in self.books if str(book.yayınTarihi) == yıl]
        if not found_books:
            print(f"'{yıl}' yılında yayınlanan kitap bulunamadı.")
        else:
            print(f"\n--- '{yıl}' Yılında Yayınlanan Kitaplar ---")
            for book in found_books:
                print(book)
            print("------------------------------------------\n")
    
    def get_book_from_api(self, isbn):
        try:
            url = f"https://openlibrary.org/api/books?bibkeys=ISBN:{isbn}&format=json&jscmd=data"
            response = httpx.get(url, timeout=10.0)
            response.raise_for_status()  # Hatalı HTTP yanıtları için hata fırlatır
            data = response.json()

            if f"ISBN:{isbn}" in data:
                book_data = data[f"ISBN:{isbn}"]
                eserAdı = book_data.get("title", "Bilinmiyor")
                yazar = ", ".join([a.get("name", "Bilinmiyor") for a in book_data.get("authors", [])])
                yayınTarihi = book_data.get("publish_date", "Bilinmiyor")
                
                # Yeni bir Book nesnesi oluşturuyoruz
                new_book = Book(eserAdı, yazar, yayınTarihi, isbn)
                print("API'den kitap bilgileri başarıyla çekildi.")
                return new_book
            else:
                print(f"Hata: {isbn} ISBN numaralı kitap API'de bulunamadı.")
                return None
        except httpx.RequestError as e:
            print(f"API isteği sırasında bir hata oluştu: {e}")
            return None
    