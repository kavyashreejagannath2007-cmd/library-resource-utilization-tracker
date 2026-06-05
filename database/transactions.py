```python
from datetime import date

from database.db_connection import (
    transactions_collection
)

from database.books import (
    get_book,
    update_book_quantity
)


def issue_book(student_id,
               student_name,
               book_id):

    book = get_book(book_id)

    if not book:
        return False, "Book not found."

    if book["quantity"] <= 0:
        return False, "Book not available."

    transaction = {
        "student_id": student_id,
        "student_name": student_name,
        "book_id": book_id,
        "book_title": book["title"],
        "issue_date": str(date.today()),
        "status": "Issued"
    }

    transactions_collection.insert_one(
        transaction
    )

    update_book_quantity(
        book_id,
        -1
    )

    return True, "Book Issued Successfully."


def return_book(book_id):

    record = transactions_collection.find_one(
        {
            "book_id": book_id,
            "status": "Issued"
        }
    )

    if not record:
        return False, "Issued record not found."

    transactions_collection.update_one(
        {
            "_id": record["_id"]
        },
        {
            "$set": {
                "status": "Returned",
                "return_date": str(date.today())
            }
        }
    )

    update_book_quantity(
        book_id,
        1
    )

    return True, "Book Returned Successfully."


def get_all_transactions():

    return list(
        transactions_collection.find(
            {},
            {"_id": 0}
        )
    )


def get_issued_books():

    return list(
        transactions_collection.find(
            {
                "status": "Issued"
            },
            {"_id": 0}
        )
    )
```
