import sympy as sp
from fractions import Fraction

def solve_proportion(a, b, c, d):
    """Solve for the missing value in a proportion a/b = c/d."""
    if a == "x":
        return (c * b) / d
    elif b == "x":
        return (a * d) / c
    elif c == "x":
        return (a * d) / b
    elif d == "x":
        return (c * b) / a
    else:
        return "Invalid input. One value must be 'x'"

def solve_for_x(equation):
    """Solve a simple algebraic equation for x."""
    x = sp.Symbol('x')
    solution = sp.solve(equation, x)
    return solution

def factor_square_root(n):
    """Factor a square root in simplified radical form."""
    return sp.simplify(sp.sqrt(n))

def decimal_to_fraction(decimal):
    """Convert decimal to fraction and percent."""
    fraction = Fraction(decimal).limit_denominator()
    percent = decimal * 100
    return fraction, f"{percent}%"

def fraction_to_decimal(fraction):
    """Convert fraction to decimal and percent."""
    decimal = float(Fraction(fraction))
    percent = decimal * 100
    return decimal, f"{percent}%"

def percent_to_other(percent):
    """Convert percent to decimal and fraction."""
    decimal = percent / 100
    fraction = Fraction(decimal).limit_denominator()
    return decimal, fraction

# Example usage:
print("Solve Proportion (2/x = 3/6):", solve_proportion(2, "x", 3, 6))
print("Solve for x (2x + 3 = 7):", solve_for_x("2*x + 3 - 7"))
print("Factor Square Root (50):", factor_square_root(50))
print("Decimal to Fraction (0.75):", decimal_to_fraction(0.75))
print("Fraction to Decimal (3/4):", fraction_to_decimal("3/4"))
print("Percent to Decimal/Fraction (75%):", percent_to_other(75))
