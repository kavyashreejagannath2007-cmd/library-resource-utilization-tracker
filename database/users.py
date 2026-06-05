```python
from database.db_connection import users_collection


def add_user(user_id, name, department, email):

    user = {
        "user_id": user_id,
        "name": name,
        "department": department,
        "email": email
    }

    users_collection.insert_one(user)


def get_all_users():

    return list(
        users_collection.find(
            {},
            {"_id": 0}
        )
    )


def get_user(user_id):

    return users_collection.find_one(
        {"user_id": user_id}
    )


def delete_user(user_id):

    users_collection.delete_one(
        {"user_id": user_id}
    )
```
