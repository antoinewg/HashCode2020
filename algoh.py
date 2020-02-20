from classes import Library
from utils import get_sorted_libraries, get_library_to_signup

def handle(lines):
    num_books, num_libraries, total_days = list(map(int, lines[0].split()))
    book_scores = list(map(int, lines[1].split()))

    libraries = []
    for i in range(num_libraries):
        _, signup_time, num_book_shippable = list(map(int, lines[2 + 2 * i].split()))
        books = list(map(int, lines[2 + 2 * i + 1].split()))

        libraries.append(Library(i, books, signup_time, num_book_shippable))


    sorted_libraries = get_sorted_libraries(libraries)

    current_day = 0
    ordered_libraries = []

    while current_day < total_days:
        msg = f"Current day {current_day}/{total_days}."
        
        library_to_signup = get_library_to_signup(libraries)
        if library_to_signup:
            ordered_libraries.append(library_to_signup)
            msg += f" Signing up {library_to_signup}"
            library_to_signup.signing_up = True
            library_to_signup.decrement_sign_up_time()
        else:
            msg += " No library to sign up."
        
        print(msg)


        current_day += 1

    res = [str(len(ordered_libraries))]
    for library in ordered_libraries:
        res.append(f"{library.id} {len(library.books_to_send)}")
        res.append(" ".join(list(map(str, library.books_to_send))))

    return res