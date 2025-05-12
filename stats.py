def get_num_words(text):
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
            list.append({"char":char,"num":chars[char]})
    return list

def sort_list(list):
    def sort_on(dict):
        return dict["num"]
    
    list.sort(reverse=True, key=sort_on)
    return list