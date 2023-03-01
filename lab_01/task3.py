import math
import pylab
import functions


def function(x, y):
    return x ** 2 + y ** 2  # функция первой производной


def picard1(x):
    return x ** 3 / 3


def picard2(x):
    return picard1(x) + x ** 7 / 63


def picard3(x):
    return picard2(x) + (x ** 11) * (2 / 2079) + (x ** 15) / 59535


def picard4(x):
    return picard3(x) + (x ** 15) * (2 / 93555) + (x ** 19) * (2 / 3393495) + (x ** 19) * (2 / 2488563) + \
           (x ** 23) * (2 / 86266215) + (x ** 23) * (1 / 99411543) + (x ** 27) * (2 / 3341878155) + (x ** 31) * (
                       1 / 109876902975)


def check_format(item):
    if type(item) == float:
        if item > 1000000:
            return '{:.4e}'.format(item)
        return '{:.4f}'.format(item)

    elif type(item) == int:
        return str(item)
    else:
        return item


def get_graphics(y1, y2, y3, y4, y5, xlist):
    pylab.xlabel('x')
    pylab.ylabel('u(x)')
    pylab.plot(xlist, y5, label="Метод Эйлера")
    pylab.plot(xlist, y1, label="1-e приближение Пикара")
    pylab.plot(xlist, y2, label="2-e приближение Пикара")
    pylab.plot(xlist, y3, label="3-e приближение Пикара")
    pylab.plot(xlist, y4, label="4-e приближение Пикара")
    pylab.legend(loc='upper left')
    pylab.title("График функции")
    pylab.show()


def main():
    x_start = 0  # начальное значение
    x_end = 2  # конечное значение
    x_end_minus = -2

    h = 1e-6  # приближение

    n = math.ceil(abs(x_end - x_start) / h) + 1  # число итераций ~ 4000
    output_step = int(n / 200)  # выводим только 200 значений в таблице

    while True:
        print("Меню")
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
            answer_euler = functions.euler(n, h, 0, 0, function)
            print(
                "------------------------------------------------------------------------------------------")
            print(
                "|         |    Метод     |__________________________Метод Пикара_________________________|")
            print(
                "|    x    |    Эйлера    |               |               |               |               |")
            print(
                "|         |    явный     |   1-е прибл.  |   2-е прибл.  |   3-е прибл.  |   4-е прибл.  |")
            print(
                "------------------------------------------------------------------------------------------")

            for i in range(0, n, output_step):
                print("|{:^9.2f}|{:^14s}|{:^15.2f}|{:^15.2f}|{:^15.2f}|{:^15.2f}|".format(x_start,
                                                                                          check_format(answer_euler[i]),
                                                                                          picard1(x_start),
                                                                                          picard2(x_start),
                                                                                          picard3(x_start),
                                                                                          picard4(x_start)))
                x_start += h * output_step
            print()

        elif c == 2:
            answer_euler1 = functions.euler(n, h, 0, 0, function)
            answer_euler2 = functions.euler(n, -h, 0, 0, function)
            answer_euler2.reverse()
            res_euler = answer_euler2 + answer_euler1

            xlist = []
            ypicard1 = []
            ypicard2 = []
            ypicard3 = []
            ypicard4 = []
            yeuler = []

            for i in range(0, 2 * n, output_step):
                xlist.append(x_end_minus)
                ypicard1.append(picard1(x_end_minus))
                ypicard2.append(picard2(x_end_minus))
                ypicard3.append(picard3(x_end_minus))
                ypicard4.append(picard4(x_end_minus))
                yeuler.append(res_euler[i])
                x_end_minus += h * output_step

            get_graphics(ypicard1, ypicard2, ypicard3, ypicard3, yeuler, xlist)
            print()


if __name__ == "__main__":
    main()
