from stats import count_words
from stats import count_characters

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words_counter = count_words(text)
    count_character_counter = count_characters(text)
    print(count_character_counter)
    return text, count_words_counter

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()