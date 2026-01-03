from stats import word_count, count_chars, char_sort
import sys

def get_book_text(location):
    with open(location) as f:
        file_contents = f.read()
    return file_contents


def main():
    if (len(sys.argv) != 2):
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_loc =sys.argv[1]
    book_text = get_book_text(book_loc)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {book_loc}...")
    print("----------- Word Count ----------")
    total_words = word_count(book_text)
    print(f"Found {total_words} total words")
    char_dict = char_sort(count_chars(book_text))
    print("--------- Character Count -------")
    for dict in char_dict:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")   

main()