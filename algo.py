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
        print(f"Current day {current_day}/{total_days}.")
        
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
            books_to_scan = get_books_to_scan([signed_up_library], newly_scanned_books)
                
            for library_books in map(set, books_to_scan.values()):
                # all_scanned_books |= set(books_to_scan.values())
                newly_scanned_books = newly_scanned_books.union(library_books)

            if books_to_scan:
                for lib_id in books_to_scan:
                    books = books_to_scan[lib_id]
                    library = libraries[lib_id]
                    library.books_to_scan += books
                    # print(f"Scanned books {books} for library {lib_id}")

        if not library_currently_signing_up.signed_up():
            # print(f" Signing up {library_currently_signing_up}")
            library_currently_signing_up.decrement_sign_up_time()
        else:
            # print(" No library to sign up.")
            pass

        current_day += 1

    res = [str(len(ordered_libraries))]
    for library in ordered_libraries:
        assert len(library.books_to_scan) <= len(library.books), "Too many books to scan"
        res.append(f"{library.id} {len(library.books_to_scan)}")
        res.append(" ".join(list(map(str, library.books_to_scan))))

    return res
