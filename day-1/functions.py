# def functionName(arguments):
#     code
#     return value
import math

def hello():
    print('hello')


def helloWorld():
    print('hello world')


def addition(a, b):
    print(a + b)
    # shadows the global a
    a = 20


def multiplication(a, b, c):
    print(a * b * c)


def factorial(number):
    result = 1
    for i in range(1, number + 1):
        result *= i
    return result


def permutation(n, r):  # nPr
    return factorial(n) / factorial(n - r)


def combination(n, r): # nCr
    return permutation(n, r) / factorial(r)


# global
a = 10
val = factorial(4)
# f(g(x))
print(factorial(9))
print(permutation(3, 2))
print(combination(3, 3))
print(sum([1, 2, 3, 9.3, -4]))
print(max([100, 200, -67]))
print(abs(45))
print(bool('d'))
print(math.factorial(110))
