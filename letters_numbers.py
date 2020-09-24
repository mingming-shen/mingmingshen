
def letter_numbers(arguments):
    """
    不同参数类型，列表和整数
    :param arguments:
    :return:
    """
    if not arguments:
        return []
    digits = []
    if type(arguments) is list:
        for i in arguments:
            digits.append(str(i))
    elif type(arguments) is int:
        digits = list(str(arguments))

    dic = {"1": "", "2": "ABC", "3": "DEF",
           "4": "GHI", "5": "JKL", "6": "MNO",
           "7": "PQRS", "8": "TUV", "9": "WXYZ", "0": ""}
    res = []
    combinations(0, "", res, digits, dic)
    return res


def combinations(index, curs, res, digits, dic):
    """
    字母的组合
    :param index:
    :param curs:
    :param res:
    :param digits:
    :param dic:
    :return:
    """
    if len(curs) == len(digits):
        res.append(curs)
        return res
    for i in dic[digits[index]]:
        combinations(index + 1, curs + i, res, digits, dic)


print(letter_numbers([2, 3]))
print(letter_numbers(78))
