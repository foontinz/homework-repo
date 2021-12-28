import fractions


class MyFraction:
    def __init__(self, arg1, arg2):
        try:
            self.fraction = fractions.Fraction(int(arg1), int(arg2))
        except ValueError:
            print('Not accesible type for fraction')

    def __add__(self, other):
        try:
            return self.fraction + other.fraction
        except AttributeError:
            return 'one of the operands has no attribute'

    def __sub__(self, other):
        try:
            return type(self.fraction)
        except AttributeError:
            return 'one of the operands has no attribute'

    def __mul__(self, other):
        try:
            return self.fraction * other.fraction
        except AttributeError:
            return 'one of the operands has no attribute'

    def __truediv__(self, other):
        try:
            return self.fraction / other.fraction
        except AttributeError:
            return 'one of the operands has no attribute'


