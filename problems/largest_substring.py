import timeit


def longest_common_substring(str1, str2):
    max_string = ""
    for i in range(len(str1)):
        for j in range(len(str1) - i):
            if (str1[i:i + j + 1] in str2):
                if (j > len(max_string)):
                    max_string = str1[i:i + j + 1]
    return max_string

#
# def longest_common_substring(str1, str2):
#     max_length = 0
#     end_index = 0
#
#     # Create a 2D array to store lengths of longest common suffixes of substrings
#     dp = [[0] * (len(str2) + 1) for _ in range(len(str1) + 1)]
#
#     for i in range(1, len(str1) + 1):
#         for j in range(1, len(str2) + 1):
#             if str1[i - 1] == str2[j - 1]:  # Characters match
#                 dp[i][j] = dp[i - 1][j - 1] + 1
#                 if dp[i][j] > max_length:  # Update maximum length and end index
#                     max_length = dp[i][j]
#                     end_index = i  # End index of substring in str1
#
#     # Return the longest common substring
#     return str1[end_index - max_length:end_index]


str1 = "GeeksForGeekstwoforever"
str2 = "GeekonetwoforeverhelloGeeks"
execution_time = timeit.timeit(
    'longest_common_substring(str1, str2)',
    globals=globals(),
    number=1000  # Number of times to run the test
)


print(f"Longest common substring: {longest_common_substring(str1, str2)}")
print(f"Execution time: {execution_time:.6f} seconds")

# Example usage

print(longest_common_substring("GeeksForGeekstwoforever", "GeekonetwoforeverhelloGeeks"))
