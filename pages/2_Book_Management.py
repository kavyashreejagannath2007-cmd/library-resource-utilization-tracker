```python
# pages/2_Book_Management.py

import streamlit as st
import pandas as pd

from database.books import (
    add_book,
    get_all_books,
    delete_book
)

st.set_page_config(
    page_title="Book Management",
    page_icon="📚",
    layout="wide"
)

st.title("📚 Book Management")

menu = st.tabs([
    "➕ Add Book",
    "📖 View Books",
    "❌ Delete Book"
])

# ---------------------------------
# Add Book
# ---------------------------------

with menu[0]:

    st.subheader("Add New Book")

    book_id = st.text_input("Book ID")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    category = st.text_input("Category")

    quantity = st.number_input(
        "Quantity",
        min_value=1,
        value=1,
        step=1
    )

    if st.button("Save Book"):

        add_book(
            book_id,
            title,
            author,
            category,
            quantity
        )

        st.success("Book Added Successfully!")

# ---------------------------------
# View Books
# ---------------------------------

with menu[1]:

    st.subheader("Available Books")

    books = get_all_books()

    if books:

        df = pd.DataFrame(books)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:
        st.warning("No books found.")

# ---------------------------------
# Delete Book
# ---------------------------------

with menu[2]:

    st.subheader("Delete Book")

    delete_id = st.text_input(
        "Enter Book ID"
    )

    if st.button("Delete"):

        delete_book(delete_id)

        st.success(
            "Book Deleted Successfully!"
        )
```
