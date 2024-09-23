from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from models import Base
from data_generation import generate_data
from queries import Queries

engine = create_engine('sqlite:///database.db')
Base.metadata.create_all(engine)

Session = sessionmaker(bind=engine)
session = Session()

# generating fake data using the session
generate_data(session)

# creating an instance of the Queries class with the current session
query_instance = Queries(session)

book_with_most_pages = query_instance.get_book_with_max_pages()
print(f'Name of the book with most pages: {book_with_most_pages.title}\n'
      f'It has {book_with_most_pages.number_of_pages} pages\n'
      f'ID: {book_with_most_pages.id}\n'
      f'Category: {book_with_most_pages.category}\n'
      f'It was published on: {book_with_most_pages.publication_date}\n'
      f'Author(s): {", ".join(f"{author.name} {author.last_name}" for author in book_with_most_pages.authors)}')


average_pages = query_instance.get_average_number_of_pages()
print(f'\nAverage pages: {int(average_pages)}')


youngest = query_instance.get_youngest_author()
print(f'\nThe youngest writer is {youngest[0]} {youngest[1]}')


authors_with_no_books = query_instance.get_authors_with_no_books()
if authors_with_no_books:
    print('\nSome of the authors with no books:')
    for author in authors_with_no_books:
        print(f"{author.name} {author.last_name}")
else:
    print('\nThere is no one without a book')


authors_with_more_than_three_books = query_instance.get_authors_with_more_than_three_books()
if authors_with_more_than_three_books:
    print('\nAuthors with more than 3 books:')
    for author in authors_with_more_than_three_books:
        print(f'{author[0]} {author[1]} - {author[2]} books')
else:
    print('No authors with more than 3 books found')

session.close()