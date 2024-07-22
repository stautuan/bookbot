def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = get_num_words(text)
    print(f"{num_of_words} of words found in this document!")


def get_book_text(path_to_file):
    with open(path_to_file) as f:
        file_content = f.read()
        return file_content


def get_num_words(text):
    words = text.split()
    word_count = 0

    for word in words:
        word_count += 1
    return word_count


main()
