def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    word_count = count_words(text)
    letter_count = character_count(text)
    letters = letter_list(letter_count)
    letters.sort(reverse=True, key=sort_on)

    print("--- Begin report of books/frankenstein.txt ---")
    print(f"{word_count} words found in the document")
    print()
    print_letters(letters)
    print("--- End Report ---")

def get_book_text(path):
    with open(path) as f:
        return f.read()


def count_words(text):
    words = text.split()
    return len(words)


def character_count(text):
    lowered = text.lower()
    letter_dict = {}
    for letter in lowered:
        if letter in letter_dict:
            letter_dict[letter] += 1 
        else:
            letter_dict[letter] = 1
    return letter_dict


def sort_on(dict):
    return dict["num"]

def letter_list(dict):
    list = []
    for c in dict:
        if c.isalpha():
            list.append({"letter": c, "num": dict[c]})
    return list

def print_letters(list):
    for dict in list:
        print(f"The '{dict['letter']}' character was found {dict['num']} times")

main()