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
