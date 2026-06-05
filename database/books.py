```python
from database.db_connection import books_collection


def add_book(book_id, title, author, category, quantity):

    book = {
        "book_id": book_id,
        "title": title,
        "author": author,
        "category": category,
        "quantity": quantity
    }

    books_collection.insert_one(book)


def get_all_books():

    return list(
        books_collection.find(
            {},
            {"_id": 0}
        )
    )


def get_book(book_id):

    return books_collection.find_one(
        {"book_id": book_id}
    )


def update_book_quantity(book_id, value):

    books_collection.update_one(
        {"book_id": book_id},
        {"$inc": {"quantity": value}}
    )


def delete_book(book_id):

    books_collection.delete_one(
        {"book_id": book_id}
    )
```
