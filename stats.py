def count_words(text):
    num_words = len(text.split())
    print(f"{num_words} words found in the document")

def char_count(text):
    char_count = {}
    for char in text:
        char = char.lower()
        if char not in char_count:
            char_count[char] = 0
        char_count[char] += 1
    return char_count

def dict_to_list(char_count):
    char_list = []
    for char, count in char_count.items():
        char_list.append({'char': char, 'count': count})
    return char_list


def print_char_count(char_list):
    for item in char_list:
        char = item['char']
        count = item['count']
        if char.isalpha():
            print(f"{char}: {count}")
