def main():
    book_path = "books/frankenstein.txt"
    book_text = get_book_text(book_path)
    num_words = count_words(book_text)
    chars_dict = character_count(book_text)
    chars_list = chars_to_list(chars_dict)
    sorted_list = sort_list(chars_list)

    report = generate_report(num_words, sorted_list)

    print(report)
    
    


def get_book_text(path):
    with open(path) as f:
        return f.read()   


def count_words(text):
    return len(text.split())


def character_count(text):
    lowercase_text = text.lower()
    char_counts = {}
    for char in lowercase_text:
        if char in char_counts:
            char_counts[char] += 1
        else:
            char_counts[char] = 1
    return char_counts


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

