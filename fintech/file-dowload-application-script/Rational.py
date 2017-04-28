#Based on PyCharm Tutorial - https://www.jetbrains.com/help/pycharm/2016.3/pycharm-refactoring-tutorial.html
from collections import namedtuple


class Rational(namedtuple('Rational', ['num', 'denom'])):

    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be null')
        if denom < 0:
            num, denom = -num, -denom
        return super().__new__(cls, num, denom)

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)


second=Rational(1,2)
third=Rational(1,3)
print(second)
print(third)



#Simplifying rational number
#Simplify a rational number by dividing numerator and denominator by the greatest common divisor:

from collections import namedtuple

class Rational(namedtuple('Rational', ['num', 'denom'])):
    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be null')
        if denom < 0:
            num, denom = -num, -denom

        x = abs(num)
        y = abs(denom)
        while x:
            x, y = y % x, x
        factor = y

        return super().__new__(cls, num // factor, denom // factor)

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)

fourth=Rational(1,4)
print(fourth)


''' Extracting a method
Extract the search for a greatest common divisor to a separate method. To do that, select the statements
x = abs(num)
        y = abs(denom)
        while x:
            x, y = y % x, x
        factor = y

Click on Refactor, Method, a dialog box opens and name the new method gcd and click on OK


'''
from collections import namedtuple

class Rational(namedtuple('Rational', ['num', 'denom'])):
    def __new__(cls, num, denom):
        if denom == 0:
            raise ValueError('Denominator cannot be null')
        if denom < 0:
            num, denom = -num, -denom

        factor = Rational.gcd(denom, num)

        return super().__new__(cls, num // factor, denom // factor)

    @staticmethod
    def gcd(denom, num):
        x = abs(num)
        y = abs(denom)
        while x:
            x, y = y % x, x
        factor = y
        return factor

    def __str__(self):
        return '{}/{}'.format(self.num, self.denom)

fourth=Rational(1,4)
print(fourth)








'''
Function and method arguments:
Always use self for the first argument to instance methods.
Always use cls for the first argument to class methods
'''


