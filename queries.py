from sqlalchemy import func
from models import Author, Book, many_to_many_relationship


class Queries:
    def __init__(self,session):
        self.session = session

    def get_book_with_max_pages(self):
        return self.session.query(Book).order_by(Book.number_of_pages.desc()).first()

    def get_average_number_of_pages(self):
        return self.session.query(func.avg(Book.number_of_pages)).scalar()

    def get_youngest_author(self):
        return self.session.query(Author.name, Author.last_name).order_by(Author.date_of_birth.desc()).first()

    def get_authors_with_no_books(self):
        return (
            self.session.query(Author)
            .outerjoin(many_to_many_relationship, Author.id == many_to_many_relationship.c.author_id) # left join with the relationship table
            .outerjoin(Book, Book.id == many_to_many_relationship.c.book_id) # left join with the Book table (books)
            .filter(Book.id is None)
            .all()
        )

    def get_authors_with_more_than_three_books(self):
        return (
            self.session.query(Author.name, Author.last_name, func.count(Book.id).label('book_count'))
            .join(many_to_many_relationship, Author.id == many_to_many_relationship.c.author_id) # inner join with the authors_books table
            .join(Book, Book.id == many_to_many_relationship.c.book_id) # inner join with the Book table (named books)
            .group_by(Author.id)
            .having(func.count(Book.id) > 3)
            .limit(5)
            .all()
        )

