# Have the user enter a number
# and find all Prime Factors (if there are any)
# and display them.
import math


# A function to print all prime factors of
# a given number n


def primeFactors(n):
    while n % 2 == 0:  # Проверить, если n делится на 2 без остатка,

        print(2)  # то печатать 2(наименьший делитель)
        n = n / 2  # и n присвоить значение n делённое на 2

    # n должен быть нечетным в этой точке
    for i in range(3, int(math.sqrt(n)) + 1, 2):  # поэтому можно использовать пропуск 2 (i = i + 2)

        # while i divides n , print i ad divide n
        while n % i == 0:
            print(i)
            n = n / i
    # Condition if n is a prime
    # number greater than 2
    if n > 2:
        print(n)


n = 315
primeFactors(n)
