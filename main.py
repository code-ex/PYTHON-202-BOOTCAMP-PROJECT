from library import Library
from book import Book
import httpx # httpx kütüphanesini içe aktardım

def main():
    library = Library()

    while True:
        print("\n--- Kütüphane Yönetim Sistemi ---")
        print("1. Kitap Ekle (Manuel)")
        print("2. Kitap Ekle (API'den)") # burası da API'den çekme kısmı
        print("3. Kitap Sil")
        print("4. Kitapları Listele")
        print("5. Gelişmiş Arama")
        print("6. Çıkış")

        choice = input("Seçiminizi girin: ")

        if choice == '1':
            eserAdı = input("Eser adı: ")
            yazar = input("Yazar adı: ")
            isbn = input("ISBN: ")
            yayınTarihi = input("Yayın tarihi: ")
            new_book = Book(eserAdı, yazar, yayınTarihi, isbn)
            library.add_book(new_book)
        elif choice == '2':
            isbn = input("Eklemek istediğiniz kitabın ISBN'ini girin: ")
            book = library.get_book_from_api(isbn)
            if book:
                library.add_book(book)
        elif choice == '3':
            isbn = input("Silmek istediğiniz kitabın ISBN'ini girin: ")
            library.remove_book(isbn)
        elif choice == '4':
            library.list_books()
        elif choice == '5':
            print("\n--- Gelişmiş Arama Seçenekleri ---")
            print("1. Yazara Göre Ara")
            print("2. Yayın Tarihine Göre Ara")
            search_choice = input("Seçiminizi girin: ")
            if search_choice == '1':
                yazar_adı = input("Yazar adını girin: ")
                library.find_by_author(yazar_adı)
            elif search_choice == '2':
                yıl = input("Yayın tarihini girin: ")
                library.find_by_publication_year(yıl)
            else:
                print("Geçersiz seçim.")
        elif choice == '6':
            print("Çıkış yapılıyor...")
            break
        else:
            print("Geçersiz seçim. Lütfen tekrar deneyin.")

if __name__ == "__main__":
    main()