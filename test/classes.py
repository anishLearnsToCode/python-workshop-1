import sympy

class Person:
    def __init__(self, firstName, lastname):
        self.firstName = firstName
        self.lastName = lastname

    def fullName(self):
        return self.firstName + ' ' + self.lastName


anish = Person('anish', 'sachdeva')
john = Person('john', 'doe')
print(anish.fullName())
print(john.fullName())
print(sympy.isprime(2))
