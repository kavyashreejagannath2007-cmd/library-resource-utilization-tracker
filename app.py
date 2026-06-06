import streamlit as st
from pymongo import MongoClient
import pandas as pd
import plotly.express as px
from datetime import date

# ==============================
# Page Config (MUST be first)
# ==============================
st.set_page_config(
    page_title="Library Resource Tracker",
    page_icon="📚",
    layout="wide"
)

# ==============================
# MongoDB Connection
# ==============================
# NOTE: Replace with MongoDB Atlas when deploying
client = MongoClient("mongodb+srv://admin:admin123@cluster0.m1eq2gp.mongodb.net/library_tracker?retryWrites=true&w=majority")
db = client["library_tracker"]

books = db["books"]
users = db["users"]
transactions = db["transactions"]

# ==============================
# Title
# ==============================
st.title("📚 Library Resource Utilization Tracker")

# ==============================
# Sidebar Menu
# ==============================
menu = st.sidebar.radio(
    "Menu",
    ["Dashboard", "Add Book", "View Books", "Add User", "Issue Book", "Return Book", "Analytics"]
)

# ==============================
# DASHBOARD
# ==============================
if menu == "Dashboard":

    st.subheader("📊 Dashboard Overview")

    total_books = books.count_documents({})
    total_users = users.count_documents({})
    total_transactions = transactions.count_documents({})
    issued_books = transactions.count_documents({"status": "Issued"})

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("Total Books", total_books)
    col2.metric("Total Users", total_users)
    col3.metric("Books Issued", issued_books)
    col4.metric("Transactions", total_transactions)

    st.markdown("---")
    st.subheader("Recent Transactions")

    data = list(transactions.find({}, {"_id": 0}).limit(10))

    if data:
        st.dataframe(pd.DataFrame(data), use_container_width=True)
    else:
        st.info("No transactions found.")

# ==============================
# ADD BOOK
# ==============================
elif menu == "Add Book":

    st.subheader("➕ Add New Book")

    book_id = st.text_input("Book ID")
    title = st.text_input("Book Title")
    author = st.text_input("Author")
    category = st.text_input("Category")
    quantity = st.number_input("Quantity", min_value=1, step=1)

    if st.button("Save Book"):

        if book_id and title:

            books.insert_one({
                "book_id": book_id,
                "title": title,
                "author": author,
                "category": category,
                "quantity": quantity
            })

            st.success("Book Added Successfully!")
        else:
            st.error("Please fill required fields!")

# ==============================
# VIEW BOOKS
# ==============================
elif menu == "View Books":

    st.subheader("📖 Available Books")

    data = list(books.find({}, {"_id": 0}))

    if data:
        st.dataframe(pd.DataFrame(data), use_container_width=True)
    else:
        st.warning("No books found.")

# ==============================
# ADD USER
# ==============================
elif menu == "Add User":

    st.subheader("👨‍🎓 Register User")

    user_id = st.text_input("User ID")
    name = st.text_input("Name")
    department = st.text_input("Department")
    email = st.text_input("Email")

    if st.button("Register"):

        if user_id and name:

            users.insert_one({
                "user_id": user_id,
                "name": name,
                "department": department,
                "email": email
            })

            st.success("User Registered Successfully!")
        else:
            st.error("Fill required fields!")

# ==============================
# ISSUE BOOK
# ==============================
elif menu == "Issue Book":

    st.subheader("📕 Issue Book")

    student_id = st.text_input("Student ID")
    student_name = st.text_input("Student Name")
    book_id = st.text_input("Book ID")

    if st.button("Issue Book"):

        book = books.find_one({"book_id": book_id})

        if book and book["quantity"] > 0:

            transactions.insert_one({
                "student_id": student_id,
                "student_name": student_name,
                "book_id": book_id,
                "book_title": book["title"],
                "issue_date": str(date.today()),
                "status": "Issued"
            })

            books.update_one(
                {"book_id": book_id},
                {"$inc": {"quantity": -1}}
            )

            st.success("Book Issued Successfully!")

        elif book:
            st.error("Book Not Available!")
        else:
            st.error("Invalid Book ID!")

# ==============================
# RETURN BOOK
# ==============================
elif menu == "Return Book":

    st.subheader("📗 Return Book")

    book_id = st.text_input("Book ID")

    if st.button("Return Book"):

        record = transactions.find_one({
            "book_id": book_id,
            "status": "Issued"
        })

        if record:

            transactions.update_one(
                {"_id": record["_id"]},
                {"$set": {"status": "Returned", "return_date": str(date.today())}}
            )

            books.update_one(
                {"book_id": book_id},
                {"$inc": {"quantity": 1}}
            )

            st.success("Book Returned Successfully!")

        else:
            st.error("No Issued Record Found!")

# ==============================
# ANALYTICS
# ==============================
elif menu == "Analytics":

    st.subheader("📊 Library Analytics")

    records = list(transactions.find({}, {"_id": 0}))

    if records:

        df = pd.DataFrame(records)

        usage = df["book_title"].value_counts().reset_index()
        usage.columns = ["Book Title", "Borrow Count"]

        st.write("### Most Borrowed Books")

        fig = px.bar(usage, x="Book Title", y="Borrow Count", text="Borrow Count")
        st.plotly_chart(fig, use_container_width=True)

        st.dataframe(usage, use_container_width=True)

        status = df["status"].value_counts().reset_index()
        status.columns = ["Status", "Count"]

        pie = px.pie(status, names="Status", values="Count")
        st.plotly_chart(pie, use_container_width=True)

    else:
        st.info("No transaction data available.")
