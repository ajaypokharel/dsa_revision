def permutation_with_spaces(s):
    op = ""
    op += s[0]
    s = s[1:]
    return helper(s, op, [])


def helper(s, op, out):
    if len(s) == 0:
        out.append(op)
        return

    helper(s[1:], op + " " + s[0], out)
    helper(s[1:], op + s[0], out)

    return out


x = permutation_with_spaces("ABC")
print(x)