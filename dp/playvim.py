
def subset_sum(arr, target):
    table = ([[False for i in range(target + 1)]
              for j in range((len(arr)) + 1)])

    for i in range(len(arr) + 1):
        table[i][0] = True

    for i in range(1, target + 1):
        table[0][i] = False

    for i in range(1, len(arr) + 1):
        for j in range(1, target + 1):
            if j < arr[i - 1]:
                table[i][j] = table[i - 1][j]
            if j >= arr[i - 1]:
                table[i][j] = (table[i - 1][j] or
                               table[i - 1][j - arr[i - 1]])

    return table[len(arr)][target]


lst = [1, 2, 7, 4, 5]
target_sum = 99

x = subset_sum(lst, target_sum)

print(x)
