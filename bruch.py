__author__ = 'Chris'

class Bruch(object):
    """
    Created on 15.01.2015
    @author: Chris
    """
    zaehler = 0
    nenner = 1

    def __init__(self, arg1=None, arg2=None):
        """
        :param arg1: numerator or a Bruch instance that is to be used instead of n/d
        :param arg2: denominator
        :return:
        """
        if isinstance(arg1, Bruch) and arg2 is None:
            self.zaehler = arg1.zaehler
            self.nenner = arg1.nenner
        elif isinstance(arg1, int):
            self.zaehler = arg1
            if isinstance(arg2, int):
                if arg2 == 0:
                    raise ZeroDivisionError("Division with 0 is not defined")
                elif arg1 < 0 and arg2 < 0:
                    self.zaehler = abs(arg1)
                    self.nenner = abs(arg2)
                else:
                    self.nenner = arg2
            elif isinstance(arg2, float):
                raise TypeError("Only int or \"Bruch\" class allowed")
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __eq__(self, other):
        """
        :param self: it's the convention
        :param other: the object which equality should be checked
        :return: True: if both objects are equal, else return False
        """
        return float(self) == float(other)

    def __ne__(self, other):
        """
        :param self: it's the convention
        :param other: the object which diversity should be checked
        :return: True: if the objects are different, else return False
        """
        return float(self) != float(other)

    def __ge__(self, other):
        """
        :param self: it's the convention
        :param other: the object which size should be checked
        :return: True: if self is greater or equal with other, else return False
        """
        return float(self) >= float(other)

    def __le__(self, other):
        """
        :param self: it's the convention
        :param other: the object which size should be checked
        :return: True: if self is lower or equal with other, else return False
        """
        return float(self) <= float(other)

    def __gt__(self, other):
        """
        :param self: it's the convention
        :param other: the object which size should be checked
        :return: True: if self is greater than other, else return False
        """
        return float(self) > float(other)

    def __lt__(self, other):
        """
        :param self: it's the convention
        :param other: the object which size should be checked
        :return: True: if self is lower than other, else return False
        """
        return float(self) < float(other)

    def __str__(self):
        """
        :param self: it's the convention
        :return: returns the converted bruch object as a string
        """
        if self.nenner == 1:
            return "(%s)" % self.zaehler
        else:
            return "(%s/%s)" % (self.zaehler, self.nenner)

    def __float__(self):
        """
        :param self: it's the convention
        :return: returns the converted value of self as a float type
        """
        return float(self.zaehler / self.nenner)

    def __abs__(self):
        """
        :param self: it's the convention
        :return: returns the abstract value of the bruch object
        """
        return Bruch(abs(self.zaehler), abs(self.nenner))

    def __int__(self):
        """
        :param self: it's the convention
        :return: returns the converted value of self as an int value
        """
        return int(self.zaehler / self.nenner)

    def __invert__(self):
        """
        :param self: it's the convention
        :return: returns the inversted bruch object, zaehler and nenner are swapped
        """
        return Bruch(self.nenner, self.zaehler)

    def __add__(b1, b2):
        """
        :param self: it's the convention
        :param b1: first addend
        :param b2: second addend
        :return: returns the sum of the addends as a bruch object
        """
        if isinstance(b2, Bruch):
            if b1.nenner != b2.nenner:
                return Bruch(b1.zaehler * b2.nenner + b2.zaehler * b1.nenner, b1.nenner * b2.nenner)
            else:
                return Bruch(b1.zaehler + b2.zaehler, b1.nenner)
        elif isinstance(b2, int):
            return b1 + Bruch(b2)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __iadd__(b1, b2):
        """
        :param self: it's the convention
        :param b1: first addend
        :param b2: second addend
        :return: returns the sum of the addends as a bruch object
        """
        if isinstance(b2, Bruch):
            return b1 + b2
        elif isinstance(b2, int):
            return b1 + Bruch(b2)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __radd__(b1, b2):
        """
        :param self: it's the convention
        :param b1: first addend
        :param b2: second addend
        :return: returns the sum of the addends as a bruch object
        """
        if isinstance(b2, int):
            return b1 + Bruch(b2)

    def __sub__(self, other=None):
        """
        :param self: it's the convention
        :param other: second subtrahend
        :return: returns the difference of both subtrahends as a bruch object
        """
        if isinstance(other, Bruch):
            if self.nenner != other.nenner:
                return Bruch(self.zaehler * other.nenner - other.zaehler * self.nenner, self.nenner * other.nenner)
            else:
                return Bruch(self.zaehler - other.zaehler, self.nenner)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __rsub__(self, other):
        """
        :param self: it's the convention
        :param other: second subtrahend
        :return: returns the difference of both subtrahends as a bruch object
        """
        if isinstance(other, Bruch):
            return self - other
        elif isinstance(other, int):
            return self * -1 + Bruch(other)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __isub__(self, other):
        """
        :param self: it's the convention
        :param other: second subtrahend
        :return: returns the difference of both subtrahends as a bruch object
        """
        if isinstance(other, Bruch):
            return self - other
        elif isinstance(other, int):
            return self - Bruch(other)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __neg__(self):
        """
        :param self: it's the convention
        :return: returns negated value of the bruch object as a bruch object
        """
        self.nenner *= -1
        return self

    def __mul__(self, other):
        """
        :param self: it's the convention
        :param other: second multiplier
        :return: returns the multiplication of the first and second multiplier as a bruch object
        """
        if isinstance(other, Bruch):
            return Bruch(self.zaehler * other.zaehler, self.nenner * other.nenner)
        elif isinstance(other, int):
            return Bruch(self.zaehler * other, self.nenner)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __rmul__(self, other):
        """
        :param self: it's the convention
        :param other: second multiplier
        :return: returns the multiplication of the first and second multiplier as a bruch object
        """
        return self * other

    def __imul__(self, other):
        """
        :param self: it's the convention
        :param other: second multiplier
        :return: returns the multiplication of the first and second multiplier as a bruch object
        """
        if isinstance(other, Bruch):
            return self * other
        elif isinstance(other, int):
            return self * Bruch(other)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __pow__(self, power):
        """
        :param self: it's the convention
        :param power: value of the exponent
        :return: returns the bruch to the power of the value which was given as a parameter as a bruch object
        """
        if isinstance(power, int):
            if power != 0:
                tb = self
                for i in range(power - 1):
                    tb *= self
                return tb
            else:
                return 1
        else:
            raise TypeError

    def _Bruch__makeBruch(arg1, arg2=None):
        """
        :param self: it's the convention
        :param arg1: value of the zaehler
        :param arg2: value of the nenner
        :return: returns the created bruch of the 2 parameters zaehler and nenner
        """
        return Bruch(arg1, arg2)

    def __truediv__(self, other):
        """
        :param self: it's the convention
        :param other: the bruch object by which is divided
        :return: returns the solution of the division, self divided by the parameter
        """
        if isinstance(other, Bruch):
            if self.zaehler != 0 and other.zaehler != 0:
                return Bruch(self.zaehler * other.nenner, self.nenner * other.zaehler)
            else:
                raise ZeroDivisionError("Division with 0 is not definable")
        elif isinstance(other, int):
            return self / Bruch(other)
        else:
            raise TypeError("Only int or \"Bruch\" class allowed")

    def __itruediv__(self, other):
        """
        :param self: it's the convention
        :param other: the bruch object by which is divided
        :return: returns the solution of the division, self divided by the parameter
        """
        return self / other

    def __rtruediv__(self, other):
        """
        :param self: it's the convention
        :param other: the bruch object by which is divided
        :return: returns the solution of the division, self divided by the parameter
        """
        return self / other

    def __iter__(self):
        """
        :param self: it's the convention
        :return: return the tuple of the object's zaehler and nenner
        """
        return tuple([self.zaehler, self.nenner]).__iter__()