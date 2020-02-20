def get_library_to_sign_up(libraries):
  sort_libraries = sorted(libraries, key=lambda x: x.total_score, reverse=True)
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