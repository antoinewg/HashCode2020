from classes import Library, NotFoundError
from utils import get_best_library
from books import get_books_to_scan
import time
from pathlib import Path

def handle(lines):
    num_books, num_libraries, total_days = list(map(int, lines[0].split()))
    book_scores = list(map(int, lines[1].split()))

    libraries_to_signup = []
    for i in range(num_libraries):
        _, signup_time, num_book_shippable = list(map(int, lines[2 + 2 * i].split()))
        book_ids = list(map(int, lines[2 + 2 * i + 1].split()))
        books = set(book_ids)

        libraries_to_signup += [Library(i, books, signup_time, num_book_shippable, book_scores)]


    remaining_days = total_days
    checkpoint_steps = 10
    next_checkpoint = remaining_days - checkpoint_steps
    scanned_libraries = []
    start_time = time.time()
    while remaining_days > 0 :
        if remaining_days < next_checkpoint:
            seconds_left = (time.time() - start_time) / (total_days - remaining_days) * remaining_days
            print(f"Remaining days: {remaining_days}. Minutes left : {seconds_left / 60}", end="\r")
            next_checkpoint -= checkpoint_steps
        # get best library
        # Only libraries with books that should be scanned should be returned
        # Only libraries for which we have time to register AND scan some books can be returned
        try:
            library, library_index = get_best_library(libraries_to_signup, remaining_days)
        except NotFoundError as not_found_reason:
            print(f"Exiting loop on days: {not_found_reason}")
            break

        # register library
        remaining_days -= library.signup_time # We still have time to scan books thanks to gest_best_library
        library.sidned_up = True
        del libraries_to_signup[library_index]

        # plan the scanning of the best books in the library until the end of time
        books_to_scan = library.books_set_ordered_by_score[:num_book_shippable * remaining_days]

        # remove the scaned books from the other libraries
        for remaining_library in libraries_to_signup:
            remaining_library.books_set_ordered_by_score -= books_to_scan

        # add the library to the results
        scanned_libraries += [
            f"{library.id} {len(library.books_to_scan)}",
            " ".join(list(map(lambda book_score: str(book_score[0]), books_to_scan)))
        ]


    return [str(len(scanned_libraries))] + scanned_libraries

