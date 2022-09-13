from collections import defaultdict


def check_anagrams(str1, str2):
    count_dict = defaultdict(int)

    for item in str1:
        count_dict[item] += 1

    for item in str2:
        count_dict[item] -= 1

    for val in count_dict.values():
        if val != 0:
            return False
    return True


def countAnagrams(str1, substring):
    if len(str1) < len(substring):
        return -1
    total = 0

    i = 0
    j = len(substring)

    while j < len(str1):
        if check_anagrams(str1[i:j], substring):
            total += 1

        i += 1
        j += 1

    return total


x = countAnagrams('cbaebabacd', 'ab')
print(x)
