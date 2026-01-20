from relationship_app.models import Author, Book, Library, Librarian

author = Author.objects.get(name="George Orwell")
books_by_author = Book.objects.filter(author=author)
print(books_by_author)

library = Library.objects.get(name="Central Library")
books_in_library = library.books.all()
print(books_in_library)

librarian = Librarian.objects.get(library=library)
print(librarian)
