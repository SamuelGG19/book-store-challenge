from datetime import datetime


class Transaction:

    SELL: int = 1
    SUPPLY: int = 2

    def __init__(self, type: int, copies: int):
        self.type: int = type
        self.copies: int = copies

    date: datetime = datetime.now()


class Book:

    def __init__(self, isbn: str, title: str, sale_price: float, purchase_price: float, quantity: int):
        self.isbn: str = isbn
        self.title: str = title
        self.sale_price: float = sale_price
        self.purchase_price: float = purchase_price
        self.quantity: int = quantity

    transactions: list[Transaction] = []

    def sell(self, quantity: int):
        # pass
        if self.copies > quantity:
            return False
        else:
            quantity -= self.copies
            self.transactions.append(Transaction(Transaction.SELL, self.copies))
            return True

    def supply(self, copies: int):
        self.quantity += copies
        self.transactions.append(Transaction(Transaction.SUPPLY, copies))

    def copies_sold(self) -> int:
        return Transaction.SELL

    def __str__(self) -> str:
        return f"ISBN: {self.isbn} \nTitle: {self.title} \nSale price: {self.sale_price} \nPurchase price: " \
               f"{self.purchase_price} \nQuantity: {self.quantity}"


class Bookstore:

    def __init__(self):
        self.catalog: dict[str, Book] = {}

    def add_book(self, isbn: str, title: str, sale_price: float, purchase_price: float, quantity: int):
        if isbn not in self.catalog:
            self.catalog[isbn] = Book(isbn, title, sale_price, purchase_price, quantity)

    def delete_book(self, isbn: str):
        if isbn in self.catalog:
            self.catalog.pop(isbn)

    def search_by_isbn(self, isbn: str) -> Book | None:
        if isbn in self.catalog:
            return self.catalog[isbn]
        else:
            return None

    def sell_book(self, isbn: str, copies: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        return book.sell(copies)

    def supply_book(self, isbn: str, copies: int) -> bool:
        book = self.search_by_isbn(isbn)
        if book is None:
            return False
        book.supply(copies)
        return True

    def best_selling_book(self) -> Book | None:
        pass
