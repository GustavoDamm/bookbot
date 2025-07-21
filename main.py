def main():
    book_path = "books/frankenstein.txt"
    text = get_book_text(book_path)
    count = count_words(text)
    return text, print(count, "words found in the document")

def get_book_text(path):
    with open(path) as f:
        return f.read()

def count_words(text):
    book_text_quantity = text.split()
    counter = 0
    for quantity in book_text_quantity:
        counter += 1
    return counter

main()