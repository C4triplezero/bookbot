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
        print(f"{dict['letter']}: {dict['num']}")