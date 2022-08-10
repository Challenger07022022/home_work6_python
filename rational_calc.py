from fractions import Fraction


def do_it(a, b, c):
    if c == '+':
        return Fraction(a) + Fraction(b)
    if c == '-':
        return Fraction(a) - Fraction(b)
    if c == '*':
        return Fraction(a) * Fraction(b)
    if c == '/':
        return Fraction(a) / Fraction(b)
