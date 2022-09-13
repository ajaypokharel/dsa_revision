import copy


def n_bit_binary(n):
    result = list()
    output = ""
    one_count = 0

    return helper(n, one_count, output, result)


def helper(number, count_of_one, op, res):

    if number == 0:
        res.append(op)
        return

    if count_of_one == 0:
        helper(number - 1, count_of_one + 1, op + '1', res)

    elif count_of_one > number:
        op1 = copy.copy(op)
        op1 += '0'
        helper(number - 1, count_of_one, op1, res)

    elif number >= count_of_one:
        helper(number - 1, count_of_one + 1, op + '1', res)
        helper(number - 1, count_of_one, op + '0', res)

    return res


lst = n_bit_binary(3)
print(lst)
