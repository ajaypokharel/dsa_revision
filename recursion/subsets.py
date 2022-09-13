import copy


def subsets(arr):
    op = []
    return helper(arr, op, [])


def helper(ip, op, result):

    if len(ip) == 0:
        result.append(op)
        return

    op1 = copy.copy(op)
    op1.append(ip[0])
    helper(ip[1:], op1, result)
    helper(ip[1:], op, result)

    return result


x = subsets([1,2, 3])

print(x)
