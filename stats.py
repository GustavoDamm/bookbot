def count_words(text):
    book_text_quantity = text.split()
    words_counter = 0
    for quantity in book_text_quantity:
        words_counter += 1
    return words_counter

def count_characters(text):
    lowercase_input = text.lower()
    dictionary_count = {}
    for i in lowercase_input:
        if i in dictionary_count:
            dictionary_count[i] += 1    
        else:
            dictionary_count[i] = 1
    return dictionary_count
