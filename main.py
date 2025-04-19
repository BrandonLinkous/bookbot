from stats import count_words
from stats import char_count
from stats import print_char_count
from stats import dict_to_list
import sys
    
def main():
    file_path = sys.argv[1]

    with open(file_path, 'r') as f:
        text = f.read()

    char_count_result = char_count(text)
    char_list = dict_to_list(char_count_result)
    char_list.sort(key=lambda item: item['count'], reverse=True)

    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {file_path}...")
    print("----------- Word Count ----------")
    word_count = len(text.split())
    print(f"Found {word_count} total words")
    print("--------- Character Count -------")
    print_char_count(char_list)
    print("============= END ===============")

if len(sys.argv) != 2:
    print("Usage: python3 main.py <path_to_book>")
    sys.exit(1)
else:
    main()