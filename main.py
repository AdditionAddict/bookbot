from stats import count_words, count_letters, print_letter_report

def get_book(book_name):
    file_path = f'./books/{book_name}.txt'
    with open(file_path, 'r') as f:
        file_contents = f.read()
        return file_contents

def main():
    book_name = 'frankenstein'
    book_content = get_book(book_name)
    word_count = count_words(book_content)
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at books/{book_name}.txt... ")
    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")
    letter_count_dict = count_letters(book_content)
    print("--------- Character Count -------")
    print_letter_report(letter_count_dict)
    print("============= END ===============")


main()
