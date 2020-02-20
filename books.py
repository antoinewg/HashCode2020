import itertools

def get_books_to_scan(signed_up_libraries, scanned_books):
    for library in signed_up_libraries:
        library.books = library.books.difference(scanned_books)
    return {
        lib.id: list(itertools.islice(library.books, lib.num_book_shippable)) for lib in signed_up_libraries
    }
