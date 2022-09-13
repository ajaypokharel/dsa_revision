def knapsack(weight_array, profit_array, max_weight):
    memo = []
    temp = []
    for i in range(len(weight_array)):
        for j in range(max_weight):
            temp.append(-1)
        memo.append(temp)

    arr_len = len(weight_array) - 1

    return knapsack_helper(weight_array, profit_array, max_weight, arr_len, memo)


def knapsack_helper(weight_array, profit_array, max_weight, arr_len, memo):
    if arr_len == 0 or max_weight == 0:
        return 0

    if memo[arr_len][max_weight] != -1:
        return memo[arr_len][max_weight]

    if weight_array[arr_len - 1] <= max_weight:
        memo[arr_len][max_weight] = max(
            profit_array[arr_len - 1] + knapsack_helper(weight_array, profit_array,
                                                        max_weight - weight_array[arr_len - 1], arr_len - 1, memo),
            knapsack_helper(weight_array, profit_array, max_weight, arr_len - 1, memo)
        )
    elif weight_array[arr_len - 1] > max_weight:
        memo[arr_len][max_weight] = knapsack_helper(weight_array, profit_array, max_weight, arr_len - 1, memo)

    return memo[arr_len][max_weight]


weight_lst = [1, 2, 7, 4]
profit_lst = [8, 5, 2, 9]
w = 12

soln = knapsack(weight_lst, profit_lst, w)

print(soln)
