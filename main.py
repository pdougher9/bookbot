from stats import num_words, num_char, sort_dict
import sys

def get_book_text(file: str) -> str:
    with open(file) as f:
        return f.read()

def main():
    if len(sys.argv) < 2:
        print("Usage: python3 main.py <path_to_book>")
    else:
        book_path = sys.argv[1]
        book_text = get_book_text(book_path)
        word_count = num_words(book_text)
        character_counts = num_char(book_text)
        sorted_characters = sort_dict(character_counts)

        print("============ BOOKBOT ============")
        print(f"Analyzing book found at {book_path}...")
        print("----------- Word Count ----------")
        print(f"Found {word_count} total words")
        print("--------- Character Count -------")
        for each in sorted_characters:
            if each['character'].isalpha():
                char_print = each['character']
                count_print = each['count']
                print(f'{char_print}: {count_print}')
        print("============= END ===============")

if __name__ == "__main__":
    main()