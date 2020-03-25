# Enter a number and have the program generate
# the Fibonacci sequence to that number or to the Nth number.


def gen_fib(n):
    a = 1
    b = 1
    for x in range(n):
        a, b = b, a+b
        yield a


for i in gen_fib(15):
    print(i)

