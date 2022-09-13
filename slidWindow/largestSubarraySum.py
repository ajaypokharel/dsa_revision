

def total_sum(arr):
    total = 0
    for item in arr:
        total += item

    return total


def largest_subarray_sum(arr, target):
    largest_len = 0
    i = 0
    j = 0

    while j <= len(arr):

        subarray_sum = total_sum(arr[i:j])
        if subarray_sum == target:
            if largest_len < len(arr[i:j]):
                largest_len = len(arr[i:j])
            i += 1
        elif subarray_sum < target:
            j += 1
        elif subarray_sum > target:
            i += 1

    return largest_len


x = largest_subarray_sum([4, 1, 1, 1, 2, 3, 1, 1, 1, 1, 1, 5], 5)
print(x)
