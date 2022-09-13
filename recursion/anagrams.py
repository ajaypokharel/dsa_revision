import copy


def generate_anagrams(letters):
    result = []
    op = ''
    return helper(letters, op, result)


def helper(ip, op, result):

    if len(ip) == 0:
        result.append(op)
        return

    for i in range(len(ip)):
        new_ip = ip[:i] + ip[i+1:]
        new_op = op + ip[i]
        helper(new_ip, new_op, result)

    return result


x = generate_anagrams('ABC')
print(x)