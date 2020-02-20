from classes import Library
from utils import get_books_to_scan, get_library_to_signup

def handle(lines):
    num_books, num_libraries, total_days = list(map(int, lines[0].split()))
    book_scores = list(map(int, lines[1].split()))

    libraries = {}
    for i in range(num_libraries):
        _, signup_time, num_book_shippable = list(map(int, lines[2 + 2 * i].split()))
        books = list(map(int, lines[2 + 2 * i + 1].split()))

        libraries[i] = (Library(i, books, signup_time, num_book_shippable))


    current_day = 0
    ordered_libraries = []
    scanned_books = {}

    while current_day < total_days:
        msg = f"Current day {current_day}/{total_days}."
        
        library_to_signup = get_library_to_signup(libraries.values())
        if library_to_signup:
            ordered_libraries.append(library_to_signup.id)
            msg += f" Signing up {library_to_signup}"
            library_to_signup.signing_up = True
            library_to_signup.decrement_sign_up_time()
        else:
            msg += " No library to sign up."
        
        print(msg)

        signed_up_libraries = [lib for lib in  libraries if lib.signed_up()]
        print(f"{len(signed_up_libraries)} libraries signed up.")

        books_to_scan = get_books_to_scan(signed_up_libraries, scanned_books)

        if books_to_scan:
            import ipdb
        
            ipdb.set_trace()
            for lib_id in books_to_scan:
                books = books_to_scan[lib_id]
                library = libraries[lib_id]
                library.books_to_scan = books
                print(f"Scanned books {books} for library {lib_id}")

        current_day += 1

    res = [str(len(ordered_libraries))]
    for library_id in ordered_libraries:
        res.append(f"{library.id} {len(library.books_to_scan)}")
        res.append(" ".join(list(map(str, library.books_to_scan))))

    return res