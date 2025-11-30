from stats import get_num_words,get_word_count, chars_list_to_sorted_list, sys

def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    else:
        book_path = sys.argv[1]
    text = get_book_text(book_path)
    num_words = get_num_words(text)
    letter_count = get_word_count(text)
    chars_sorted_list = chars_list_to_sorted_list(letter_count)
    print_sorted(book_path, num_words, chars_sorted_list)

def get_book_text(path):
    with open(path) as f:
        return f.read()


def print_sorted(book_path, num_words, chars_sorted_list):
    print( "========= BOOKBOT =========" ) 
    print( f"Analyzing book found at {book_path}" ) 
    print( "--------- Word Count ---------" ) 
    print( f"Found {num_words} total words" ) 
    print( "--------- Character Count ---------" )
    for item in chars_sorted_list:
        if not item["char"].isalpha():
            continue
        print(f"{item["char"]}: {item["num"]}")
    print("========= END =========")


main()
