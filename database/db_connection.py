from pymongo import MongoClient
import streamlit as st

# MongoDB URI
MONGO_URI = st.secrets["MONGO_URI"]

# Create MongoDB client
client = MongoClient(MONGO_URI)

# Database
db = client["library_tracker"]

# Collections
books_collection = db["books"]
users_collection = db["users"]
transactions_collection = db["transactions"]


def get_database():
    return db


def get_books_collection():
    return books_collection


def get_users_collection():
    return users_collection


def get_transactions_collection():
    return transactions_collection
