def count_words(content):
    return len(content.split())
def count_letters(content):
    letters_dict = {}
    for c in content:
        if not c.isalpha():
            continue
        if c in letters_dict:
            letters_dict[c] += 1
        else:
            letters_dict[c] = 1
    return letters_dict
def main():
    with open("./books/frankenstein.txt") as f:
        content = f.read()
        words_count = count_words(content)
        print("--- Begin report of books/frankenstein.txt ---")
        print(f"{words_count} words found in the document")
        print("\n")
        letters = count_letters(content.lower())
        letters = dict(sorted(letters.items(), reverse=True,key=lambda item: item[1]))
        for letter, val in letters.items():
            print(f"The '{letter}' character was found {val} times")
        print("--- End report ---")


main()
