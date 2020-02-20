def get_sorted_libraries(libraries):
  return libraries

def get_library_to_signup(libraries):
  """
  Returns the most promising library to sign up at some point.
  If one library is still signing up, we return this library.
  """
  signing_up = [lib for lib in libraries if lib.signing_up]

  if len(signing_up) and signing_up[0].time_left_to_signup > 0:
    return signing_up[0]

  not_signed_up = [lib for lib in libraries if not lib.signed_up()]
  if len(not_signed_up):
    return not_signed_up[0]
  
  return None


def get_books_to_scan(signed_up_libraries, scanned_books):
  return {lib.id: lib.books[:lib.num_book_shippable] for lib in signed_up_libraries}