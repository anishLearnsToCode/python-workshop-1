from math import factorial
from math import pi
from math import gcd
import random

# print(math.pi)
# print(math.factorial(5))
# print(math.gcd(3, 6))
# print(factorial(6))
# print(pi)
# print(gcd(9, 43))
# print(random.randint(1, 1000))
# print(int(random.random() * 1000))


def isPrime(number):
    if number == 0 or number == 1:
        return False

    for i in range(2, number):
        if number % i == 0:
            return False

    return True

print(isPrime(0))
print(isPrime(1))
print(isPrime(2))
print(isPrime(3))
print(isPrime(4))
print(isPrime(5))
print(isPrime(6))
print(isPrime(7))
