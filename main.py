def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    num_of_words = get_num_words(text)
    num_of_characters = get_num_characters(text)
    character_list = dict_to_list(num_of_characters)

    print(f"--- Begin report of {book_path} ---")
    print(f"{num_of_words} of words found in the document")

    for c in character_list:
        if c["character"].isalpha():
            print(f"The {c["character"]} was found {c["num"]} times")

    print("--- End report ---")


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


def dict_to_list(dict):
    dict_list = []

    for d in dict:
        dict_list.append({"character": d, "num": dict[d]})
    dict_list.sort(reverse=True, key=sort_on)
    return dict_list


def sort_on(dict):
    return dict["num"]


main()
