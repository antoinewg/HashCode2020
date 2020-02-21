from classes import NotFoundError
from operator import itemgetter

def get_library_to_sign_up(libraries):
  sort_libraries = sorted(libraries, key=lambda x: x.num_book_shippable * x.total_score / x.signup_time, reverse=True)
  return sort_libraries[0]


def get_library_to_signup(libraries, ordered_libraries):
  """
  Returns the most promising library to sign up at some point.
  If one library is still signing up, we return this library.
  """
  signing_up = [lib for lib in libraries if lib.signing_up]

  # If one of the library is already signing up, we return this library
  if len(signing_up) and signing_up[0].time_left_to_signup > 0:
    signing_up[0].signing_up = True
    return ordered_libraries + [signing_up[0]]

  not_signed_up = [lib for lib in libraries if not lib.signed_up()]
  if len(not_signed_up):
    library_to_sign_up = get_library_to_sign_up(not_signed_up)
    library_to_sign_up.signing_up = True
    return ordered_libraries + [library_to_sign_up]
  
  return ordered_libraries

def get_best_library(libraries, days_left):

    if len(libraries) == 0:
        raise NotFoundError("No more libraries")

    def score(library):
        return sum(
                map(itemgetter(1), 
                    library.books_set_ordered_by_score[
                        :library.num_book_shippable * (days_left-library.signup_time)
                    ]),
                    0
                    )
    library_scores = {
            library.id: score(library) if library.signup_time < days_left else 0
            for library in libraries
    }
    libraries = sorted(libraries, key=lambda library: library_scores[library.id], reverse=True)
    best_library = libraries[0]

    if best_library.signup_time >= days_left:
        raise NotFoundError("No library to signup in the remaining time")

    return best_library, libraries[1:]
