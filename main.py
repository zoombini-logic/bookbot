from stats import word_count, count_chars, char_sort

def get_book_text(location):
    with open(location) as f:
        file_contents = f.read()
    return file_contents


def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print("============ BOOKBOT ============")
    print("Analyzing book found at books/frankenstein.txt...")
    print("----------- Word Count ----------")
    total_words = word_count(book_text)
    print(f"Found {total_words} total words")
    char_dict = char_sort(count_chars(book_text))
    print("--------- Character Count -------")
    for dict in char_dict:
        if dict["char"].isalpha():
            print(f"{dict["char"]}: {dict["num"]}")   

main()