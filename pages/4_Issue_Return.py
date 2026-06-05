```python
# pages/4_Issue_Return.py

import streamlit as st
import pandas as pd

from database.transactions import (
    issue_book,
    return_book,
    get_all_transactions
)

st.set_page_config(
    page_title="Issue & Return",
    page_icon="🔄",
    layout="wide"
)

st.title("🔄 Book Issue & Return Management")

tab1, tab2, tab3 = st.tabs(
    [
        "📕 Issue Book",
        "📗 Return Book",
        "📋 Transaction History"
    ]
)

# ----------------------------------------
# Issue Book
# ----------------------------------------

with tab1:

    st.subheader("Issue a Book")

    student_id = st.text_input(
        "Student ID"
    )

    student_name = st.text_input(
        "Student Name"
    )

    book_id = st.text_input(
        "Book ID"
    )

    if st.button("Issue Book"):

        success, message = issue_book(
            student_id,
            student_name,
            book_id
        )

        if success:
            st.success(message)
        else:
            st.error(message)

# ----------------------------------------
# Return Book
# ----------------------------------------

with tab2:

    st.subheader("Return a Book")

    return_book_id = st.text_input(
        "Enter Book ID"
    )

    if st.button("Return Book"):

        success, message = return_book(
            return_book_id
        )

        if success:
            st.success(message)
        else:
            st.error(message)

# ----------------------------------------
# Transaction History
# ----------------------------------------

with tab3:

    st.subheader("Library Transactions")

    records = get_all_transactions()

    if records:

        df = pd.DataFrame(records)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.info(
            "No transaction records available."
        )
```
