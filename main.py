def get_book(book_name):
    file_path = f'./books/{book_name}.txt'
    with open(file_path, 'r') as f:
        file_contents = f.read()
        return file_contents

def count_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    letter_map = { x : 0 for x in 'abcdefghijklmnopqrstuvwxyz' }
    for letter in content:
        letter = letter.lower()
        if letter in letter_map:
            letter_map[letter] += 1
    
    return letter_map

def print_letter_report(letter_count_dict):
    # create sorted list of letter counts
    letter_count_list = sorted(letter_count_dict.items(), key=lambda x: x[1], reverse=True)

    for letter, count in letter_count_list:
        print(f"The character '{letter}' appears {count} times.") 


def main():
    book_name = 'frankenstein'
    book_content = get_book(book_name)
    word_count = count_words(book_content)
    print(f"--- Beging report for book {book_name} ---")
    print(f"{word_count} words found in the document.\n")
    letter_count_dict = count_letters(book_content)
    print_letter_report(letter_count_dict)
    print(f"\n--- End report for book {book_name} ---")


main()
