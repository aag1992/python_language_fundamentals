lst = ["cat", "dog", "god", "tac", "act"]


def get_anagram_indices(lst):
    dict = {}
    sorted_lst = [''.join(sorted(elem)) for elem in lst]
    for i,elem in enumerate(sorted_lst):
        if elem in dict:
            dict[elem].add(i)
        else:
            dict[elem] = {i}

    return dict

get_anagram_indices(lst)