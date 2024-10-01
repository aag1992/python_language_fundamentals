def find_common(str1, str2):
    if not str1 or not str2:
        print("No common letters.")
        return
    char_set_str1 = set(str1)
    char_set_str2 = set(str2)
    print("The common letters are:")
    print(char_set_str1 & char_set_str2)
