import math


def total_sum(sub):
    total = 0
    for item in sub:
        total += item
    return total


def max_sum_subarray(arr, k):

    maxSum = -math.inf

    i = 0
    j = k
    while j <= len(arr):
        temp_sum = 0
        temp_sum = total_sum(arr[i:j])
        if temp_sum > maxSum:
            maxSum = temp_sum
        i += 1
        j += 1

    return maxSum


out = max_sum_subarray([1, 2, 3, 4, 5, 6], 4)
print(out)
