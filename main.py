from stats import word_count, count_chars

def get_book_text(location):
    with open(location) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    total_words = word_count(book_text)
    print(f"Found {total_words} total words")
    char_dict = count_chars(book_text)
    print(char_dict)

main()