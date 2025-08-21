from stats import get_word_count, get_char_count, create_list_of_dict, sorted_list_of_dict
import sys

def get_book_text(filepath):
    with open(filepath, "r", encoding="utf-8") as f:
        return f.read()


def get_sort_dict(unsorted_dict):
    sorted_dict = dict=(sorted(unsorted_dict.items(), key=lambda item: item[1], reverse=True))
    return sorted_dict


def main():
    if len(sys.argv)!=2:
        print("Usage: python3 main.py <path_to_book>")
        sys.exit(1)

    filepath = sys.argv[1]
    book_text = get_book_text(filepath)

    word_count = get_word_count(book_text)
    char_count = get_char_count(book_text)
    list_of_dict = create_list_of_dict(char_count)
    sorted_list = sorted_list_of_dict(list_of_dict)

    print_report(filepath, word_count,sorted_list)



def print_report(filepath, word_count, sorted_list):
    print("============ BOOKBOT ============")
    print(f"Analyzing book found at {filepath}...")

    print("----------- Word Count ----------")
    print(f"Found {word_count} total words")

    print("--------- Character Count -------")
    for item in sorted_list:
        if item["char"].isalpha():
            print(f"{item['char']}: {item['num']}")
    print("============= END ===============")


if __name__ == "__main__":
    main()


