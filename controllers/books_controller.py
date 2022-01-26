from flask import Flask, render_template, request, redirect, Blueprint
from repositories import book_repository
from repositories import author_repository
from models.book import Book
from models.author import Author
books_blueprint = Blueprint("books", __name__)

@books_blueprint.route("/")
def home():
    return render_template('index.html')


@books_blueprint.route('/books')
def books():
    books = book_repository.select_all()
    return render_template('books/index.html', all_books = books)

@books_blueprint.route('/books/<id>/delete', methods=['POST'])
def delete_book(id):
    book_repository.delete(id)
    return redirect('/books')


@books_blueprint.route('/books/new', methods=['GET'])
def new_book():
    authors = author_repository.select_all()
    return render_template('books/new.html', all_authors = authors)

@books_blueprint.route('/books', methods=['POST'])
def add_book():
    title = request.form['title']
    author_id = request.form['author_id']
    genre = request.form['genre']
    author = author_repository.select(author_id)
    book = Book[title, author, genre]
    book_repository.save(book)
    return redirect('/books')
