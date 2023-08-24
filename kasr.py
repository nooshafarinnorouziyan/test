class Fraction:
    def __init__(self, numerator, denominator):
        self.numerator = numerator
        self.denominator = denominator
    
    def simplify(self):
        gcd = self.find_gcd()
        self.numerator = self.numerator // gcd
        self.denominator = self.denominator // gcd

    def find_gcd(self):
        a = self.numerator
        b = self.denominator
        while b != 0:
            temp = b
            b = a % b
            a = temp
        return a
    
    def __add__(self, other):
        num = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) + (other.numerator * self.denominator)
        result = Fraction(new_numerator, num)
        result.simplify()
        return result
    
    def __sub__(self, other):
        num = self.denominator * other.denominator
        new_numerator = (self.numerator * other.denominator) - (other.numerator * self.denominator)
        result = Fraction(new_numerator, num)
        result.simplify()
        return result
    
    def __mul__(self, other):
        new_numerator = self.numerator * other.numerator
        new_denominator = self.denominator * other.denominator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result
    
    def __truediv__(self, other):
        new_numerator = self.numerator * other.denominator
        new_denominator = self.denominator * other.numerator
        result = Fraction(new_numerator, new_denominator)
        result.simplify()
        return result

    def __str__(self):
        self.simplify()
        return f"{self.numerator}/{self.denominator}"