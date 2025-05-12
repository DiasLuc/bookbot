from stats import get_num_words, character_count, chars_to_list, sort_list
import sys
def main():
    if len(sys.argv) != 2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)
    book_path = sys.argv[1]
    book_text = get_book_text(book_path)
    num_words = get_num_words(book_text)
    chars_dict = character_count(book_text)
    chars_list = chars_to_list(chars_dict)
    sorted_list = sort_list(chars_list)

    report = generate_report(book_path, num_words, sorted_list)

    print(report)
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()   


def generate_report(book_path, word_count, char_counts):
        
        print(f"============ BOOKBOT ============\nAnalyzing book found at {book_path}...")
        print(f"----------- Word Count ----------\nFound {word_count} total words")
        print("--------- Character Count -------")
        for char in char_counts:
            print(f"{char["char"]}: {char["num"]}")
        print(f"============= END ===============")

main()

