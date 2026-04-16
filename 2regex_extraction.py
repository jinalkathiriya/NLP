# regex extraction

import sqlite3
import re
import nltk
from nltk.tokenize import word_tokenize

# Download once (first run only)
nltk.download('punkt')

# Connect to database
conn = sqlite3.connect("users.db")
cursor = conn.cursor()

# Create table
cursor.execute("""
CREATE TABLE IF NOT EXISTS users (
    name TEXT,
    email TEXT,
    phone TEXT,
    date TEXT
)
""")

# Regex Patterns
email_pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
phone_pattern = r'^(?:\+91[-\s]?)?\d{10}$'
date_pattern = r'^\d{1,2}[/-]\d{1,2}[/-]\d{4}$|^\d{4}-\d{2}-\d{2}$'

# Insert Function with Validation
def insert_data():
    name = input("Enter Name: ").strip()

    if name == "":
        print("❌ Name cannot be empty")
        return

    # --- NLTK used here ---
    email_input = input("Enter Email: ")
    email_tokens = word_tokenize(email_input)
    email = "".join(email_tokens)

    if not re.match(email_pattern, email):
        print("❌ Invalid Email Format")
        return

    # --- NLTK used here ---
    phone_input = input("Enter Phone: ")
    phone_tokens = word_tokenize(phone_input)
    phone = "".join(phone_tokens)

    if not re.match(phone_pattern, phone):
        print("❌ Invalid Phone Number")
        return

    # --- NLTK used here ---
    date_input = input("Enter Date (dd/mm/yyyy or yyyy-mm-dd): ")
    date_tokens = word_tokenize(date_input)
    date = "".join(date_tokens)

    if not re.match(date_pattern, date):
        print("❌ Invalid Date Format")
        return

    cursor.execute("INSERT INTO users VALUES (?, ?, ?, ?)",
                   (name, email, phone, date))
    conn.commit()

    print("✅ Data Inserted Successfully!")

# Search Function
def search_data():
    search_name = input("Enter name to search: ")

    cursor.execute("SELECT * FROM users WHERE name = ?", (search_name,))
    result = cursor.fetchone()

    if result:
        print("\n----- User Found -----")
        print("Name:", result[0])
        print("Email:", result[1])
        print("Phone:", result[2])
        print("Date:", result[3])
    else:
        print("❌ No record found.")

# Menu
while True:
    print("\n1. Insert Data")
    print("2. Search by Name")
    print("3. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        insert_data()
    elif choice == "2":
        search_data()
    elif choice == "3":
        break
    else:
        print("Invalid choice")

conn.close()