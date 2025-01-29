def main():
    path = "books/frankenstein.txt"
    text = open_text(path)
    words_count = count_words(text)
    print(f"--- Begin report of {path} ---")
    print(f"{words_count} words found in the document\n")
    list_of_counts = sort_letters(count_chars(text))

    for count in list_of_counts:
        print(count)
    
    print("--- End report ---")

def count_words(text):
    return len(text.split())

def open_text(path):
    with open("books/frankenstein.txt") as f:
        return f.read()
    
def count_chars(text):
    alpha_dict = {}
    text_low = text.lower()
    alphabet = "abcdefghijklmnopqrstuvwxyz"
    for letter in text_low:
        if letter.isalpha():
            if letter in alpha_dict:
                alpha_dict[letter] += 1
            else:
                alpha_dict[letter] = 1

    return alpha_dict

def sort_letters(dict):
    list = []
    strings_list = []
    for letter in dict:
        list.append(dict[letter])
    list.sort(reverse=True)
    for i in range(0, len(list)):
        for letter in dict:
            if dict[letter] == list[i]:
                strings_list.append(f"The '{letter}' character was found {list[i]} times")

    return strings_list

main()