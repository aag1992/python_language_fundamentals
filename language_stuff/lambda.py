from functools import reduce


lst = [-1, 1 , 4, -12, 2, -4, 12,1]
def sort_by_lambda(list):
    f = lambda x : x**2

    sorted_list = sorted(list)
    print(sorted_list)

    sorted_squares_list = sorted(sorted_list, key=f)
    print(sorted_squares_list)

# sort_by_lambda(list)


def filter_by_lambda(lst):
    f = lambda x: x %2 ==0
    filtered_list = list(filter(f, lst))
    print(filtered_list)

# filter_by_lambda(lst)

def reduce_by_lambda(lst):
    f = lambda x,y: x *y
    product = reduce(f, lst)
    print(product)

reduce_by_lambda(lst)
