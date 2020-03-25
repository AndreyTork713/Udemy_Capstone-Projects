# Just like the previous problem, but with e instead of PI.
# Enter a number and have the program generate e up to that many decimal places.
# Keep a limit to how far the program will go.

#import math

dig = float(input("Введите число: "))
precision = int(input('Введите количество знаков после запятой: '))

while precision >= 15:
    print('Слишком большое число...')
    precision = int(input('Введите количество знаков после запятой: '))
print('%.*f' %(precision, dig))
