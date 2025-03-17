def get_book_text(filepath): # Defines everything for rest of program
    with open(filepath) as f:
        book_text = f.read() # Reads contents of specified file in path
        return book_text

def count_words(text): # Word count feature. Uses .split() method
    words = text.split()
    return len(words)

def main():
    book_text = get_book_text("books/dracula.txt")
    word_count = count_words(book_text)
    print(f"{word_count} words found in this document man")

# def main(): (original def for main to generate contents)
#     book_text = get_book_text("books/dracula.txt")
#     print(book_text) - defined in first function

main()