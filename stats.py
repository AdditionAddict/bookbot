def count_words(content):
    words = content.split()
    return len(words)

def count_letters(content):
    letter_map = {}
    for letter in content:
        letter = letter.lower()
        if letter in letter_map:
            letter_map[letter] += 1
        else:
            letter_map[letter] = 1
        
    
    return letter_map

def print_letter_report(letter_count_dict):
    # create sorted list of letter counts
    letter_count_list = sorted(letter_count_dict.items(), key=lambda x: x[1], reverse=True)

    for letter, count in letter_count_list:
        if not letter.isalpha():
            continue
        print(f"{letter}: {count}") 