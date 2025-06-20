from stats import count_words, character_count, sort_on, letter_list, print_letters
import sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
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


main()