import pdb
from models.author import Author
from models.book import Book

import repositories.author_repository as author_repository
import repositories.book_repository as book_repository

book_repository.delete_all()
author_repository.delete_all()

author1 = Author("Ian", "Rankin")
author_repository.save(author1)
author2 = Author("Lee", "Child")
author_repository.save(author2)

book1 = Book("Rebus", author1, "crime")
book_repository.save(book1)

book2 = Book("Another Rebus", author1, "crime")
book_repository.save(book2)

book3 = Book("Jack Reacher", author2, "thriller")
book_repository.save(book3)

author_repository.select(1)

pdb.set_trace()