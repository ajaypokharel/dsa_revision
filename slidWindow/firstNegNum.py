def find_neg(arr):
    neg = 0
    for item in arr:
        if item < 0:
            neg = item
            break
    return neg


def first_neg_number(arr, k):
    output_array = []

    i = 0
    j = k

    while j <= len(arr):
        neg = find_neg(arr[i:j])
        output_array.append(neg)
        i += 1
        j += 1

    return output_array


x = first_neg_number([1, -2, 3, -3, -5, 9, 4, 5], 4)
print(x)
