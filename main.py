from stats import count_words
from stats import count_characters
from stats import sort_on

def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count_words_counter = count_words(text)
    count_character_counter = count_characters(text)
    char_list = []

    for char in count_character_counter:
        if char.isalpha():
            char_list.append({"char": char, "num": count_character_counter[char]})
    char_list.sort(reverse=True, key=sort_on)

    
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_path}...")
    print("----------- Word Count ----------")
    print(f"Found {count_words_counter} total words")
    print(f"--------- Character Count -------")
    for i in char_list:
        print(f"{i["char"]}: {i["num"]}")
    print("============= END ===============")

def get_book_text(path):
    with open(path) as f:
        return f.read()

main()