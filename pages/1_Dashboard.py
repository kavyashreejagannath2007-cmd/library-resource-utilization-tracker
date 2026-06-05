```python
# pages/1_Dashboard.py

import streamlit as st
import pandas as pd

from database.db_connection import (
    books_collection,
    users_collection,
    transactions_collection
)

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide"
)

st.title("📚 Library Dashboard")

# --------------------------------
# Metrics
# --------------------------------

total_books = books_collection.count_documents({})
total_users = users_collection.count_documents({})
issued_books = transactions_collection.count_documents(
    {"status": "Issued"}
)
returned_books = transactions_collection.count_documents(
    {"status": "Returned"}
)

col1, col2, col3, col4 = st.columns(4)

col1.metric(
    "📖 Total Books",
    total_books
)

col2.metric(
    "👨‍🎓 Total Users",
    total_users
)

col3.metric(
    "📕 Books Issued",
    issued_books
)

col4.metric(
    "📗 Books Returned",
    returned_books
)

st.divider()

# --------------------------------
# Recent Transactions
# --------------------------------

st.subheader("🔄 Recent Transactions")

transactions = list(
    transactions_collection.find(
        {},
        {"_id": 0}
    ).sort("_id", -1).limit(10)
)

if transactions:

    df = pd.DataFrame(transactions)

    st.dataframe(
        df,
        use_container_width=True
    )

else:
    st.info(
        "No transactions available."
    )

st.divider()

# --------------------------------
# Available Books
# --------------------------------

st.subheader("📚 Available Books")

books = list(
    books_collection.find(
        {},
        {"_id": 0}
    )
)

if books:

    df_books = pd.DataFrame(books)

    st.dataframe(
        df_books,
        use_container_width=True
    )

else:
    st.warning(
        "No books found."
    )

st.divider()

# --------------------------------
# Registered Users
# --------------------------------

st.subheader("👨‍💻 Registered Users")

users = list(
    users_collection.find(
        {},
        {"_id": 0}
    )
)

if users:

    df_users = pd.DataFrame(users)

    st.dataframe(
        df_users,
        use_container_width=True
    )

else:
    st.warning(
        "No users registered."
    )

st.success("Dashboard Loaded Successfully!")
```
