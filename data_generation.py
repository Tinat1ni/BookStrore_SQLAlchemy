from faker import Faker
import random
from models import Author, Book
from datetime import datetime

fake = Faker()

categories = ['Fiction', 'Horror', 'Science', 'History',
              'Biography', 'Fantasy', 'Mystery', 'Romance']

today = datetime.today().date()

def generate_data(session, num_authors=500, num_books=1000):
    authors_data = []
    for _ in range(num_authors):
        author = Author(
            name=fake.first_name(),
            last_name=fake.last_name(),
            date_of_birth=fake.date_of_birth(),
            birth_place=fake.city()
        )
        authors_data.append(author)

    session.add_all(authors_data)
    session.commit()

    for _ in range(num_books):
        author = random.choice(authors_data)
        book = Book(
            title=fake.sentence(nb_words=4),
            category=random.choice(categories),
            number_of_pages=fake.random_int(min=100, max=1600),
            publication_date=fake.date_between_dates(date_start=author.date_of_birth, date_end=today)
        )
        session.add(book)
        book.authors.append(author)

    session.commit()