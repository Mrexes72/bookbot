def get_num_words(text):
    words = text.split()
    return len(words)

def get_chars_dict(text):
    words = text.split()
    character_count = {}
    for word in words:
        for letter in word:
            letter = letter.lower()
            if letter in character_count:
                character_count[letter] += 1
            else:
                character_count[letter] = 1
    return character_count

def sort_on(d):
    return d["num"]


def chars_dict_to_sorted_list(num_chars_dict):
    sorted_list = []
    for ch in num_chars_dict:
        sorted_list.append({"char": ch, "num": num_chars_dict[ch]})
    sorted_list.sort(key=sort_on, reverse=True)
    return sorted_list
    