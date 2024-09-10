import pandas as pd
from faker import Faker
import random
from datetime import datetime, timedelta

fake = Faker()

# Number of records to generate
num_libraries = 5
num_books = 100
num_users = 50
num_loans = 70
num_holds = 30

# 1. Generate Libraries Data
def generate_libraries(num):
    libraries = []
    for i in range(num):
        libraries.append({
            'library_id': i + 1,
            'library_name': fake.company(),
            'location': fake.city()
        })
    return pd.DataFrame(libraries)

# 2. Generate Categories Data (for books)
categories = ['Self-Improvement', 'Biography', 'Fantasy', 'Romance', 'Science Fiction']
categories_df = pd.DataFrame({'category_id': list(range(1, len(categories)+1)), 'category_name': categories})

# 3. Generate Books Data
def generate_books(num, num_libraries, categories):
    books = []
    for i in range(num):
        books.append({
            'book_id': i + 1,
            'title': fake.sentence(nb_words=3),
            'author': fake.name(),
            'category_id': random.randint(1, len(categories)),
            'library_id': random.randint(1, num_libraries),
            'quantity': random.randint(1, 20)
        })
    return pd.DataFrame(books)

# 4. Generate Users Data
def generate_users(num):
    users = []
    for i in range(num):
        users.append({
            'user_id': i + 1,
            'username': fake.user_name(),
            'email': fake.email()
        })
    return pd.DataFrame(users)

# 5. Generate Loans Data
def generate_loans(num, num_users, num_books, num_libraries):
    loans = []
    for i in range(num):
        loan_date = fake.date_between(start_date='-1y', end_date='today')
        due_date = loan_date + timedelta(days=14)
        return_date = loan_date + timedelta(days=random.randint(1, 20)) if random.random() < 0.8 else None
        loans.append({
            'loan_id': i + 1,
            'user_id': random.randint(1, num_users),
            'book_id': random.randint(1, num_books),
            'library_id': random.randint(1, num_libraries),
            'loan_date': loan_date,
            'due_date': due_date,
            'return_date': return_date
        })
    return pd.DataFrame(loans)

# 6. Generate Holds Data
def generate_holds(num, num_users, num_books, num_libraries):
    holds = []
    for i in range(num):
        hold_date = fake.date_between(start_date='-6m', end_date='today')
        hold_expiry_date = hold_date + timedelta(days=7)
        holds.append({
            'hold_id': i + 1,
            'user_id': random.randint(1, num_users),
            'book_id': random.randint(1, num_books),
            'library_id': random.randint(1, num_libraries),
            'hold_date': hold_date,
            'hold_expiry_date': hold_expiry_date
        })
    return pd.DataFrame(holds)

# Generate the datasets
libraries_df = generate_libraries(num_libraries)
books_df = generate_books(num_books, num_libraries, categories)
users_df = generate_users(num_users)
loans_df = generate_loans(num_loans, num_users, num_books, num_libraries)
holds_df = generate_holds(num_holds, num_users, num_books, num_libraries)

# Save datasets to CSV files
libraries_df.to_csv('libraries.csv', index=False)
categories_df.to_csv('categories.csv', index=False)
books_df.to_csv('books.csv', index=False)
users_df.to_csv('users.csv', index=False)
loans_df.to_csv('loans.csv', index=False)
holds_df.to_csv('holds.csv', index=False)

print("Dummy data generated and saved to CSV files.")

