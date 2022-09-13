import copy


def generate_parenthesis(n):
    result_list = list()
    close_brac = n
    open_brac = n
    output = ''

    return helper(open_brac, close_brac, output, result_list)


def helper(open_bracket, close_bracket, out_string, result):

    if open_bracket == 0 and close_bracket == 0:
        result.append(out_string)
        return

    if open_bracket != 0:
        op1 = copy.copy(out_string)
        op1 += '('
        helper(open_bracket - 1, close_bracket, op1, result)

    if close_bracket > open_bracket:
        op2 = copy.copy(out_string)
        op2 += ')'
        helper(open_bracket, close_bracket - 1, op2, result)

    return result


lst = generate_parenthesis(3)
print(lst)