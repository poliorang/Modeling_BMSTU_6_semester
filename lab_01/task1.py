import math
import pylab
import functions


def function(x, y):
    return y ** 2 + x  # функция первой производной


def picard1(x):
    return (x ** 3) / 3 + x + 1


def picard2(x):
    return picard1(x) + (x ** 4) / 12 + (x ** 2) / 2


def picard3(x):
    return picard2(x) + (x ** 5) / 60 + (x ** 3) / 6


def picard4(x):
    return picard3(x) + (x ** 6) / 360 + (x ** 4) / 24


def analit(x):
    return 3 * math.exp(x) - x ** 2 - 2 * x - 2


def check_format(item):
    if type(item) == float:
        if item > 1000000:
            return '{:.4e}'.format(item)
        return '{:.4f}'.format(item)

    elif type(item) == int:
        return str(item)
    else:
        return item


def get_graphics(y1, y2, y3, y4, y5, y6, xlist):
    pylab.xlabel('x')
    pylab.ylabel('u(x)')
    pylab.plot(xlist, y5, label="Метод Эйлера")
    # pylab.plot(xlist, y1, label="1-e приближение Пикара")
    # pylab.plot(xlist, y2, label="2-e приближение Пикара")
    # pylab.plot(xlist, y3, label="3-e приближение Пикара")
    # pylab.plot(xlist, y4, label="4-e приближение Пикара")
    pylab.plot(xlist, y6, label="Аналитическое решение")
    pylab.legend(loc='upper left')
    pylab.title("График функции")
    pylab.show()


def main():
    x_start = 0  # начальное значение
    x_end = 0.93  # конечное значение
    x_end_minus = 0

    h = 1e-6  # приближение

    n = math.ceil(abs(x_end - x_start) / h) + 1  # число итераций ~ 4000
    output_step = int(n / 200)  # выводим только 200 значений в таблице

    while True:
        print("Меню (задание 1)")
        print("1. Таблица")
        print("2. График")
        print("")

        while True:
            try:
                c = int(input("Выберите пункт >> "))
                if c > 2 or 1 > c:
                    raise Exception()
                break
            except Exception as e:
                print('Несуществующий пункт')
        print()
        if c == 1:
            answer_euler = functions.euler(n, h, 0, 1, function)
            print(
                "---------------------------------------------------------------------------------------------------------")
            print(
                "|         |    Метод     |     Метод     |__________________________Метод Пикара_________________________|")
            print(
                "|    x    |    Эйлера    |     Аналит    |               |               |               |               |")
            print(
                "|         |    явный     |               |   1-е прибл.  |   2-е прибл.  |   3-е прибл.  |   4-е прибл.  |")
            print(
                "---------------------------------------------------------------------------------------------------------")

            for i in range(0, n, output_step):
                print("|{:^9.2f}|{:^14s}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|".format(x_start,
                                                                                                    check_format(
                                                                                                        answer_euler[
                                                                                                            i]),
                                                                                                    analit(x_start),
                                                                                                    picard1(x_start),
                                                                                                    picard2(x_start),
                                                                                                    picard3(x_start),
                                                                                                    picard4(x_start)))
                x_start += h * output_step
            print()

        elif c == 2:
            answer_euler1 = functions.euler(n, h, 0, 1, function)
            answer_euler2 = functions.euler(n, -h, 0, 1, function)
            answer_euler2.reverse()
            res_euler = answer_euler2 + answer_euler1

            xlist = []
            ypicard1 = []
            ypicard2 = []
            ypicard3 = []
            ypicard4 = []
            yeuler = []
            yanalit = []

            for i in range(0, 2 * n, output_step):
                xlist.append(x_end_minus)
                ypicard1.append(picard1(x_end_minus))
                ypicard2.append(picard2(x_end_minus))
                ypicard3.append(picard3(x_end_minus))
                ypicard4.append(picard4(x_end_minus))
                yeuler.append(res_euler[i])
                yanalit.append(analit(x_end_minus))
                x_end_minus += h * output_step

            get_graphics(ypicard1, ypicard2, ypicard3, ypicard3, yeuler, yanalit, xlist)
            print()


if __name__ == "__main__":
    main()
