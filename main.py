from stats import get_num_words, character_count
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

    report = generate_report(num_words, sorted_list)

    print(report)
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()   







def chars_to_list(chars):
    list = []
    for char in chars:
        if char.isalpha():
            list.append({"letter":char,"count":chars[char]})
    return list

def sort_list(list):
    def sort_on(dict):
        return dict["count"]
    
    list.sort(reverse=True, key=sort_on)
    return list



def generate_report(word_count, char_counts):
        
        print(f"--- Begin report of books/frankenstein.txt ---")
        print(f"{word_count} words found in the document\n")
        for char in char_counts:
            print(f"The '{char["letter"]}' character was found {char["count"]} times")
        print(f"--- End report ---")

main()

