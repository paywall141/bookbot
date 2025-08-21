def get_word_count(text_str):
    word_array=text_str.split()
    return len(word_array)

def get_char_count(text):
    char_cnt = {}
    for char in text:
        lowered = char.lower()
        if lowered in char_cnt:
            char_cnt[lowered] += 1
        else:
            char_cnt[lowered] = 1
    return char_cnt


def create_list_of_dict(dict):
    arr = []
    for key, value in dict.items():
        arr.append({"char": key , "num": value })
    return arr

def sort_on(items):
    return items["num"]

def sorted_list_of_dict(list):
    list.sort(reverse=True, key=sort_on)
    return list
