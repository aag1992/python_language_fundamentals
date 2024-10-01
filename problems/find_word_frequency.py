import sys
from collections import Counter
from find_common_letters_two_strings import find_common


def find_frequency_of_words(sentence: str) -> dict:
    words_list = sentence.split(" ")
    words_dictionary = Counter(words_list)
    return words_dictionary



if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Please add input strings")
        exit(0)
    sentence= sys.argv[1]
    print("The words count is")
    count_dict = find_frequency_of_words(sentence)
    for item in count_dict:
        print(f"The word \"{item}\" appears {count_dict[item]} times")

