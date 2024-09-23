from sqlalchemy import Column, String, Integer, Date, ForeignKey, Table
from sqlalchemy.orm import declarative_base, relationship

Base = declarative_base() # creating a base class for declarative models

# defining ManyToMany relationship table for authors and books
many_to_many_relationship = Table(
    'authors_books',
    Base.metadata,
    Column('author_id', Integer, ForeignKey('authors.id')),
    Column('book_id', Integer, ForeignKey('books.id'))
)

# author model:
class Author(Base):
    __tablename__ = 'authors'

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String)
    last_name = Column(String)
    date_of_birth = Column(Date)
    birth_place = Column(String)
    books = relationship('Book', secondary=many_to_many_relationship, back_populates='authors')

# book model:
class Book(Base):
    __tablename__ = 'books'

    id = Column(Integer, primary_key=True, autoincrement=True)
    title = Column(String)
    category = Column(String)
    number_of_pages = Column(Integer)
    publication_date = Column(Date)
    authors = relationship('Author', secondary=many_to_many_relationship, back_populates='books')


