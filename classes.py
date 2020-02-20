class Library:
  def __init__(self, id, books, signup_time, num_book_shippable):
    self.id = id
    self.books = books
    self.signup_time = signup_time + 1
    self.num_book_shippable = num_book_shippable
    self.time_left_to_signup = signup_time + 1
    self.signing_up = False

  def decrement_sign_up_time(self):
    self.time_left_to_signup -= 1

  def signed_up(self):
    return self.time_left_to_signup == 0

  def __repr__(self):
    return f"Library [{self.id}] {len(self.books)}/{self.num_book_shippable} {self.time_left_to_signup}/{self.signup_time}"