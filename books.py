
def get_books_to_scan(signed_up_libraries, scanned_books):
  return {
        lib.id: list(lib.books.keys())[:lib.num_book_shippable] for lib in signed_up_libraries
    }
