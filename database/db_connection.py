```python
# database/db_connection.py

from pymongo import MongoClient

# MongoDB Connection URL
MONGO_URI = "mongodb://localhost:27017/"

# Create Client
client = MongoClient(MONGO_URI)

# Create / Connect Database
db = client["library_tracker"]

# Collections
books_collection = db["books"]
users_collection = db["users"]
transactions_collection = db["transactions"]


def get_database():
    """
    Returns the MongoDB database object.
    """
    return db


def get_books_collection():
    """
    Returns books collection.
    """
    return books_collection


def get_users_collection():
    """
    Returns users collection.
    """
    return users_collection


def get_transactions_collection():
    """
    Returns transactions collection.
    """
    return transactions_collection
```
