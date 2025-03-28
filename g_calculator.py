import sympy as sp
import numpy as np
import matplotlib.pyplot as plt
from ipywidgets import interact, FloatSlider

# -----------------------
# 1) GRAPH ONE OR MORE FUNCTIONS
# -----------------------
def plot_functions(func_expressions, x_range=(-10, 10), points=200):
    """
    Plot one or more functions given as strings in func_expressions.
    x_range: (min_x, max_x)
    points: number of points to plot
    """
    x = sp.Symbol('x', real=True)
    x_vals = np.linspace(x_range[0], x_range[1], points)
    
    plt.figure(figsize=(8, 5))
    
    for expr_str in func_expressions:
        try:
            expr = sp.sympify(expr_str)
            # Evaluate expression for all x values
            y_vals = [expr.subs(x, val) for val in x_vals]
            plt.plot(x_vals, y_vals, label=f"y = {expr_str}")
        except Exception as e:
            print(f"Could not parse function '{expr_str}': {e}")
    
    plt.axhline(0, color='black', linewidth=0.5)  # x-axis
    plt.axvline(0, color='black', linewidth=0.5)  # y-axis
    plt.grid(True)
    plt.legend()
    plt.title("Function Plot")
    plt.show()

# -----------------------
# 2) CREATE A TABLE OF (x, y) VALUES
# -----------------------
def create_table(func_expression, x_start=-5, x_end=5):
    """
    Create a table of (x, y) values for the given function.
    """
    x = sp.Symbol('x', real=True)
    expr = sp.sympify(func_expression)
    
    print(f"Table of (x, y) for y = {func_expression}:")
    for val in range(x_start, x_end + 1):
        y_val = expr.subs(x, val)
        print(f"x = {val}, y = {y_val}")

# -----------------------
# 3) SHADE ABOVE OR BELOW THE LINE
# -----------------------
def shade_region(func_expression, x_min=-10, x_max=10, shade_above=True):
    """
    Shade above or below the line y = f(x).
    """
    x = sp.Symbol('x', real=True)
    expr = sp.sympify(func_expression)
    
    x_vals = np.linspace(x_min, x_max, 400)
    y_vals = [expr.subs(x, val) for val in x_vals]
    
    plt.figure(figsize=(8, 5))
    plt.plot(x_vals, y_vals, label=f"y = {func_expression}", color='blue')
    
    # Shade region
    if shade_above:
        plt.fill_between(x_vals, y_vals, max(y_vals)+5, color='red', alpha=0.2, label="Shade Above")
    else:
        plt.fill_between(x_vals, y_vals, min(y_vals)-5, color='green', alpha=0.2, label="Shade Below")
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.xlim(x_min, x_max)
    plt.grid(True)
    plt.legend()
    plt.title("Shaded Region")
    plt.show()

# -----------------------
# 4) SOLVE AND GRAPH A SYSTEM OF EQUATIONS
# -----------------------
def solve_and_graph_system(equation1, equation2, x_range=(-10, 10), points=200):
    """
    Solve a system of two equations and plot them.
    equation1, equation2: strings like 'x + y - 3 = 0'
    """
    x, y = sp.symbols('x y', real=True)
    
    # Convert strings to sympy equations
    eq1_lhs, eq1_rhs = equation1.split('=')
    eq2_lhs, eq2_rhs = equation2.split('=')
    
    eq1 = sp.Eq(sp.sympify(eq1_lhs), sp.sympify(eq1_rhs))
    eq2 = sp.Eq(sp.sympify(eq2_lhs), sp.sympify(eq2_rhs))
    
    # Solve system
    solutions = sp.solve((eq1, eq2), (x, y), dict=True)
    print("Solutions to the system:")
    for sol in solutions:
        print(sol)
    
    # We'll plot each equation by solving for y in terms of x (if possible)
    # eq1: sp.solve(eq1, y) -> get y in terms of x
    def plot_equation(equation, label):
        # Attempt to solve for y in terms of x
        try:
            sol_for_y = sp.solve(equation, y)
            if not isinstance(sol_for_y, list):
                sol_for_y = [sol_for_y]
            
            x_vals = np.linspace(x_range[0], x_range[1], points)
            for idx, s in enumerate(sol_for_y):
                y_vals = [s.subs(x, val) for val in x_vals]
                plt.plot(x_vals, y_vals, label=f"{label} (branch {idx+1})")
        except Exception as e:
            print(f"Could not solve {equation} for y: {e}")
    
    plt.figure(figsize=(8, 5))
    plot_equation(eq1, 'Eq1')
    plot_equation(eq2, 'Eq2')
    
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.title("System of Equations")
    plt.show()

# -----------------------
# 5) ZOOM IN OR OUT ON A GRAPH
# -----------------------
def interactive_zoom(func_expression):
    """
    Interactive zoom in/out using sliders for x_min, x_max.
    """
    x = sp.Symbol('x', real=True)
    expr = sp.sympify(func_expression)
    
    def plot_func(xmin, xmax):
        x_vals = np.linspace(xmin, xmax, 400)
        y_vals = [expr.subs(x, val) for val in x_vals]
        plt.figure(figsize=(8, 5))
        plt.plot(x_vals, y_vals, label=f"y = {func_expression}")
        plt.axhline(0, color='black', linewidth=0.5)
        plt.axvline(0, color='black', linewidth=0.5)
        plt.grid(True)
        plt.legend()
        plt.title("Zoom In/Out")
        plt.show()
    
    interact(plot_func,
             xmin=FloatSlider(value=-10, min=-50, max=0, step=1),
             xmax=FloatSlider(value=10, min=0, max=50, step=1))

# -----------------------
# 6) SOLVE QUADRATIC EQUATIONS
# -----------------------
def solve_quadratic_equation(a, b, c):
    """
    Solve a quadratic equation ax^2 + bx + c = 0
    Returns the real solutions, if any.
    """
    x = sp.Symbol('x', real=True)
    # Create equation a*x^2 + b*x + c = 0
    eq = sp.Eq(a*x**2 + b*x + c, 0)
    solutions = sp.solve(eq, x, dict=False)
    return solutions

def plot_quadratic(a, b, c, x_range=(-10, 10), points=200):
    """
    Plot the quadratic ax^2 + bx + c over the given range.
    """
    x_vals = np.linspace(x_range[0], x_range[1], points)
    y_vals = a*x_vals**2 + b*x_vals + c
    plt.figure(figsize=(8,5))
    plt.plot(x_vals, y_vals, label=f"{a}x^2 + {b}x + {c}")
    plt.axhline(0, color='black', linewidth=0.5)
    plt.axvline(0, color='black', linewidth=0.5)
    plt.grid(True)
    plt.legend()
    plt.title("Quadratic Function")
    plt.show()

# -------------------------------------------------------
# EXAMPLE USAGE:
# (You can remove or modify these as needed for your final submission.)
# -------------------------------------------------------
if __name__ == '__main__':
    # 1) Graphing one or more functions
    print("Plotting two functions: y = x^2 and y = sin(x)")
    plot_functions(["x^2", "sin(x)"], x_range=(-5, 5))
    
    # 2) Creating a table of (x, y) values
    print("\nCreating a table for y = x^2, from x = -3 to x = 3")
    create_table("x^2", -3, 3)
    
    # 3) Shading above or below the line
    print("\nShading above y = 0.5*x + 2 from x = -5 to x = 5")
    shade_region("0.5*x + 2", x_min=-5, x_max=5, shade_above=True)
    
    # 4) Solving and graphing a system of equations
    print("\nSolving system: x + y = 3 and x - y = 1")
    solve_and_graph_system("x + y = 3", "x - y = 1", x_range=(-2, 5))
    
    # 5) Zooming in/out on a graph
    print("\nInteractive Zoom on y = x^2. Adjust sliders in Colab.")
    interactive_zoom("x^2")
    
    # 6) Solving quadratic equations
    print("\nSolving and plotting quadratic equation: 2x^2 - 4x + 1 = 0")
    sol = solve_quadratic_equation(2, -4, 1)
    print("Solutions:", sol)
    plot_quadratic(2, -4, 1, x_range=(-1, 3))
