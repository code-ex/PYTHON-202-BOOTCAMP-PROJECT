from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import List, Optional
import httpx

# Kendi Book ve Library sınıflarımı da içeri attım.
from library import Library

# Pydantic ile kendi ayarladığım veri tabanını tanımladım.
class BookSchema(BaseModel):
    eserAdı: str
    yazar: str
    yayınTarihi: str
    isbn: str

app = FastAPI()

library = Library()

# API Uç Noktaları (Endpoints)

@app.get("/books", response_model=List[BookSchema])
def get_all_books():
    """Tüm kitapları listeleme endpoint'i"""
    return library.books

@app.post("/books", response_model=BookSchema)
def add_new_book(book: BookSchema):
    """Yeni bir kitap ekleme endpoint'i"""
    # Manuel olarak yeni kitap ekleme
    new_book = Book(
        eserAdı=book.eserAdı,
        yazar=book.yazar,
        yayınTarihi=book.yayınTarihi,
        isbn=book.isbn
    )
    library.add_book(new_book)
    return new_book

@app.get("/books/{isbn}", response_model=BookSchema)
def get_book_by_isbn(isbn: str):
    """ISBN'e göre kitap bulma endpoint'i"""
    book = library.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Kitap bulunamadı")
    return book

@app.put("/books/{isbn}", response_model=BookSchema)
def update_book(isbn: str, updated_book: BookSchema):
    """ISBN'e göre kitabı güncelleyen endpoint'i"""
    book = library.find_book(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="Güncellenecek kitap bulunamadı.")
    
    # Kitap bilgilerini güncelle
    book.eserAdı = updated_book.eserAdı
    book.yazar = updated_book.yazar
    book.yayınTarihi = updated_book.yayınTarihi
    
    library.save_books() # Değişikliği dosyaya kaydet
    return book

@app.delete("/books/{isbn}")
def delete_book(isbn: str):
    """ISBN'e göre kitabı silen endpoint'i"""
    if not library.remove_book(isbn): # library sınıfındaki remove_book metodunu kullan
        raise HTTPException(status_code=404, detail="Silinecek kitap bulunamadı.")
    
    return {"message": "Kitap başarıyla silindi."}

@app.post("/books/from-api/{isbn}", response_model=BookSchema)
def add_book_from_api(isbn: str):
    """Harici API'den kitap verisi çekerek yeni kitap ekleyen endpoint'i"""
    book = library.get_book_from_api(isbn)
    if not book:
        raise HTTPException(status_code=404, detail="API'de kitap bulunamadı.")
    
    library.add_book(book)
    return book