import numpy as np
import sympy as sp

def annuity_payment(present_value, rate, time, continuous=False):
    """Calculate annuity with monthly or continuous growth."""
    if continuous:
        return present_value * np.exp(rate * time)
    else:
        return present_value * ((1 + rate) ** time)

def mortgage_payment(principal, annual_rate, months):
    """Calculate monthly mortgage payment."""
    r = annual_rate / 12
    return (principal * r) / (1 - (1 + r) ** -months)

def retirement_balance(initial, monthly_contribution, rate, years):
    """Estimate retirement balance with regular contributions."""
    months = years * 12
    r = rate / 12
    return initial * ((1 + r) ** months) + monthly_contribution * (((1 + r) ** months - 1) / r)

def doubling_time(rate):
    """Determine time until amount doubles using the rule of 72."""
    return 72 / (rate * 100)

def solve_log_equation(equation):
    """Solve logarithmic equations."""
    x = sp.Symbol('x')
    return sp.solve(equation, x)

def scientific_notation_conversion(number):
    """Convert number to and from scientific notation."""
    return "{:.6e}".format(number), float("{:.6e}".format(number))

# Example usage:
print("Annuity Growth:", annuity_payment(1000, 0.05, 10))
print("Mortgage Payment:", mortgage_payment(200000, 0.04, 360))
print("Retirement Balance:", retirement_balance(5000, 500, 0.06, 30))
print("Doubling Time:", doubling_time(0.05))
print("Solve Log Equation (log(x) = 3):", solve_log_equation("sp.log(x) - 3"))
print("Scientific Notation Conversion (123456789):", scientific_notation_conversion(123456789))
