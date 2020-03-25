# Find PI to the Nth Digit -
# Enter a number and have the program generate PI up
# to that many decimal places.
# Keep a limit to how far the program will go

import math

precision = int(input('Введите количество знаков после запятой: '))

while precision >= 15:
    print('Слишком большое число...')
    precision = int(input('Введите количество знаков после запятой: '))
print('%.*f' %(precision, math.pi))
