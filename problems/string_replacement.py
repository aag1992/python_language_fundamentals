import timeit



# def string_replacement(str, orig_chr, new_chr):
#     return str.replace(orig_chr, new_chr)

def string_replacement(str, orig_chr, new_chr):
    ret_str = ''
    for i in range(len(str)):
        if(str[i] == orig_chr):
            ret_str += new_chr
        else:
            ret_str+= str[i]
    return ret_str


def wrapper():
    return string_replacement("l vey u", " ", "o")
execution_time = timeit.timeit(wrapper, number=1000000)


print(execution_time)
# 0.0009087009966606274
# 0.00017370300338370726