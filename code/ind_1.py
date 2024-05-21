#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# С использованием многопоточности для
# заданного значения x найти сумму ряда S с
# точностью члена ряда по абсолютному
# значению e=10^-7 и произвести сравнение
# полученной суммы
# с контрольным значением функции y
# для двух бесконечных рядов.
# Варианты 29 и 30 (4 и 5)

import math
from threading import Lock, Thread

lock = Lock()


# 4 (29) вариант
def sum_row_1(x, eps, s_dict):
    s = 0
    n = 1
    while True:
        a = 1 / (2 ** n)
        b = 1 / (3 ** n)
        c = math.pow(x, n - 1)
        element = (a + b) * c

        if abs(element) < eps:
            break
        else:
            s += element
            n += 1
    with lock:
        s_dict["row_1"] = s


# 5 (30) вариант
def sum_row_2(x, eps, sum_dict):
    sum = 0
    n = 0
    f = 1
    i = 1
    while True:
        z = 2 * i
        k = x ** (2 * n)
        f *= (z - 1) * z
        element = ((-1) ** n) * k / (f / 2)
        i = n + 1

        if abs(element) < eps:
            break
        else:
            sum += element
            n += 1
    with lock:
        sum_dict["row_2"] = sum


def main():
    sum_dict = {}

    eps = 10 ** -7
    # 4 Вариант
    x1 = -0.8
    y1 = (5 - 2 * x1) / (6 - 5 * x1 + (x1 ** 2))
    # 5 Вариант
    x2 = 0.3
    y2 = math.cos(x2)

    thread1 = Thread(target=sum_row_1, args=(x1, eps, sum_dict))
    thread2 = Thread(target=sum_row_2, args=(x2, eps, sum_dict))

    thread1.start()
    thread2.start()

    thread1.join()
    thread2.join()

    sum_1 = sum_dict["row_1"]
    sum_2 = sum_dict["row_2"]

    print(
        f"Полученное значение (4 вариант): {sum_1}"
        f"\nОжидаемое значение (4 вариант): {y1}"
        f"\nРазница: {abs(sum_1 - y1)}"
    )
    print(
        f"\nПолученное значение (5 вариант): {sum_2}"
        f"\nОжидаемое значение(5 вариант)): {y2}"
        f"\nРазница: {abs(sum_2 - y2)}"
    )


if __name__ == "__main__":
    main()
