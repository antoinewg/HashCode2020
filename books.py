import itertools

def get_books_to_scan(signed_up_libraries, scanned_books):
    results = {}

    for library in signed_up_libraries:
        books_to_scan = []
        library.books = library.books.difference(scanned_books)

        for _ in range(library.num_book_shippable):
            book_candidate = None
            while book_candidate is None:
                if len(library.books_ordered_by_score) == 0:
                    break
                book_candidate = library.books_ordered_by_score.popleft()[0]
                if book_candidate in library.books:
                    books_to_scan += [book_candidate]
        results[library.id] = books_to_scan

    return results
