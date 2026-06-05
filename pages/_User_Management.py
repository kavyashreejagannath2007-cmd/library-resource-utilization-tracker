```python
# pages/_User_Management.py

import streamlit as st
import pandas as pd

from database.users import (
    add_user,
    get_all_users,
    delete_user
)

st.set_page_config(
    page_title="User Management",
    page_icon="👨‍🎓",
    layout="wide"
)

st.title("👨‍🎓 User Management")

tab1, tab2, tab3 = st.tabs(
    [
        "➕ Add User",
        "📋 View Users",
        "❌ Delete User"
    ]
)

# -----------------------------------
# Add User
# -----------------------------------

with tab1:

    st.subheader("Register New User")

    user_id = st.text_input(
        "User ID"
    )

    name = st.text_input(
        "Student Name"
    )

    department = st.text_input(
        "Department"
    )

    email = st.text_input(
        "Email Address"
    )

    if st.button("Register User"):

        add_user(
            user_id,
            name,
            department,
            email
        )

        st.success(
            "User Registered Successfully!"
        )

# -----------------------------------
# View Users
# -----------------------------------

with tab2:

    st.subheader("Registered Users")

    users = get_all_users()

    if users:

        df = pd.DataFrame(users)

        st.dataframe(
            df,
            use_container_width=True
        )

    else:

        st.warning(
            "No users found."
        )

# -----------------------------------
# Delete User
# -----------------------------------

with tab3:

    st.subheader("Delete User")

    delete_id = st.text_input(
        "Enter User ID"
    )

    if st.button("Delete User"):

        delete_user(
            delete_id
        )

        st.success(
            "User Deleted Successfully!"
        )
```
