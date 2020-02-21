from collections import deque
from operator import itemgetter

class Library:
  def __init__(self, id, books, signup_time, num_book_shippable, book_scores):
    self.id = id
    self.books = books
    self.books_ordered_by_score = deque(sorted([
        (book_id, book_scores[book_id]) 
        for book_id in books 
    ], key=itemgetter(1), reverse=True))
    self.total_score = sum([book_scores[book] for book in books])
    self.signup_time = signup_time
    self.num_book_shippable = num_book_shippable
    self.time_left_to_signup = signup_time
    self.signing_up = False
    self.books_to_scan = []

  def decrement_sign_up_time(self):
    self.time_left_to_signup -= 1

  def signed_up(self):
    return self.time_left_to_signup == 0

  def __repr__(self):
    return f"Library [{self.id}] {len(self.books)}/{self.num_book_shippable} {self.time_left_to_signup}/{self.signup_time}"

class NotFoundError(Exception):
    def __init__(self, message):
        self.message=message
