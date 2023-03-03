def euler(n, h, x, y, function):
    answer = []

    for i in range(n):
        try:
            y += h * function(x, y)
            answer.append(y)
            x += h
        except OverflowError:
            answer.append("Over")

    return answer


def check_format(item):
    if type(item) == float:
        if item > 1000000:
            return '{:.4e}'.format(item)
        return '{:.4f}'.format(item)

    elif type(item) == int:
        return str(item)
    else:
        return item