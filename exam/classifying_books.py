def classify_books(*genre_and_book, **isbn_title_of_book):
    fiction_books = []
    non_fiction_books = []

    fiction_dict = {}
    non_fiction_dict = {}


    for genre, book in genre_and_book:
        if genre == "fiction":
            fiction_books.append(book)
        elif genre == "non_fiction":
            non_fiction_books.append(book)

    for isbn, book in isbn_title_of_book.items():
        if book in fiction_books:
            fiction_dict[isbn] = book
        elif book in non_fiction_books:
            non_fiction_dict[isbn] = book

    final_fiction_list = []
    final_fiction_list.append("Fiction Books:")
    non_final_fiction_list = []
    non_final_fiction_list.append("Non-Fiction Books:")

    for key, value in sorted(fiction_dict.items(), key=lambda x: x[0]):
        final_fiction_list.append(f"~~~{key}#{value}")

    for key, value in sorted(non_fiction_dict.items(), key=lambda x: x[0], reverse=True):
        non_final_fiction_list.append(f"***{key}#{value}")

    final_output = []

    if fiction_books and non_fiction_books:
        final_output.append('\n'.join(final_fiction_list))
        final_output.append('\n'.join(non_final_fiction_list))

    elif fiction_books and not non_fiction_books:
        final_output.append('\n'.join(final_fiction_list))

    elif not fiction_books and non_fiction_books:
        final_output.append('\n'.join(non_final_fiction_list))

    return '\n'.join(final_output)

print(classify_books(
    ("non_fiction", "Sapiens"),
    ("non_fiction", "Homo Deus"),
    ("non_fiction", "The Selfish Gene"),
    NF123ABC="Sapiens",
    NF987XYZ="Homo Deus",
    NF456DEF="The Selfish Gene"
))






