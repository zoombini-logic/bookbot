def get_book_text(location):
    with open(location) as f:
        file_contents = f.read()
    return file_contents

def main():
    book_text = get_book_text("./books/frankenstein.txt")
    print(book_text)

main()