def get_sorted_libraries(libraries):
  return libraries

def get_library_to_signup(libraries, ordered_libraries):
  """
  Returns the most promising library to sign up at some point.
  If one library is still signing up, we return this library.
  """
  signing_up = [lib for lib in libraries if lib.signing_up]

  if len(signing_up) and signing_up[0].time_left_to_signup > 0:
    signing_up[0].signing_up = True
    return ordered_libraries + [signing_up[0]]

  not_signed_up = [lib for lib in libraries if not lib.signed_up()]
  if len(not_signed_up):
    not_signed_up[0].signing_up = True
    return ordered_libraries + [not_signed_up[0]]
  
  return ordered_libraries