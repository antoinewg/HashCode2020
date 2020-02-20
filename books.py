
def get_books_to_scan(signed_up_libraries, scanned_books):
  return {lib.id: lib.books[:lib.num_book_shippable] for lib in signed_up_libraries}