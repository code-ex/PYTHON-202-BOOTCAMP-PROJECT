class Book:
    def __init__(self, eserAdı, yazar, yayınTarihi, isbn):
        self.eserAdı = eserAdı
        self.yazar = yazar
        self.yayınTarihi = yayınTarihi
        self.isbn = isbn

    def __str__(self):
        return f"{self.eserAdı} - Yazar: {self.yazar} (ISBN: {self.isbn}, Yayın Tarihi: {self.yayınTarihi})"