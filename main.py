def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = get_num_words(text)
    num_of_characters = get_num_characters(text)
    print(num_of_characters)


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


def get_num_characters(text):
    word = text.lower()
    characters_dict = {}

    for w in word:
        if w in characters_dict:
            characters_dict[w] += 1
        else:
            characters_dict[w] = 1
    return characters_dict


main()
