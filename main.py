def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    print(text)


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content


main()
