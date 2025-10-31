def main():
    book_titles = []
    count = 0

    while count < 10:
        title_input = input(f"Enter book title {count + 1}: ")
        book_titles.append(title_input.title())
        count += 1

    books_sorted = sorted(book_titles)

    print("\nHere are the book titles in alphabetical order:")
    for title in books_sorted:
        print(title)

if __name__ == "__main__":
    main()