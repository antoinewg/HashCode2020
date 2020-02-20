from classes import Library
from utils import get_library_to_signup
from books import get_books_to_scan

def handle(lines):
    num_books, num_libraries, total_days = list(map(int, lines[0].split()))
    book_scores = list(map(int, lines[1].split()))

    libraries = {}
    for i in range(num_libraries):
        _, signup_time, num_book_shippable = list(map(int, lines[2 + 2 * i].split()))
        book_ids = list(map(int, lines[2 + 2 * i + 1].split()))
        books = set(book_ids)

        libraries[i] = (Library(i, books, signup_time, num_book_shippable, book_scores))


    current_day = 0
    ordered_libraries = []
    newly_scanned_books = set()
    all_scanned_books = set()

    library_currently_signing_up = None
    while current_day < total_days:
        if current_day % 100 == 0:
            print(f"Current day {current_day}/{total_days}.", end="\r")
        
        if library_currently_signing_up is None or library_currently_signing_up.signed_up():
            ordered_libraries = get_library_to_signup(
                libraries.values(),
                ordered_libraries,
            )
            library_currently_signing_up = ordered_libraries[-1]
        
        

        signed_up_libraries = [lib for lib in ordered_libraries if lib.signed_up()]
        # print(f"{len(signed_up_libraries)} libraries signed up.")

        newly_scanned_books = set()
        for signed_up_library in signed_up_libraries:
            books_to_scan = get_books_to_scan(signed_up_library, newly_scanned_books)
                
            library_books = set(books_to_scan)
            all_scanned_books |= library_books # union
            newly_scanned_books = newly_scanned_books.union(library_books)

            signed_up_library.books_to_scan += books_to_scan

        if not library_currently_signing_up.signed_up():
            # print(f"[sign up] Signing up {library_currently_signing_up}")
            library_currently_signing_up.decrement_sign_up_time()
        else:
            # print("[sign up] No library to sign up.")
            pass

        current_day += 1

    res = []
    non_empty_libs = 0
    for library in ordered_libraries:
        assert len(library.books_to_scan) <= len(library.books), "Too many books to scan"
        if len(library.books_to_scan) > 0:
            non_empty_libs += 1
            res.append(f"{library.id} {len(library.books_to_scan)}")
            res.append(" ".join(list(map(str, library.books_to_scan))))
    res = [str(non_empty_libs)] + res

    return res
