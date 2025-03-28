import numpy as np
import matplotlib.pyplot as plt
import random
import sympy as sp
from ipywidgets import interact, FloatSlider

def scatter_plot_game():
    """Generate random scatter points and ask player for coordinates."""
    x, y = random.randint(0, 10), random.randint(0, 10)
    
    plt.scatter(x, y, color='red')
    plt.xlim(0, 10)
    plt.ylim(0, 10)
    plt.grid()
    plt.title("Scatter Plot Game: Identify the (x, y) Coordinate")
    plt.show()
    
    guess_x = int(input("Enter x-coordinate: "))
    guess_y = int(input("Enter y-coordinate: "))
    
    if (guess_x, guess_y) == (x, y):
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is ({x}, {y})")

def algebra_practice_game():
    """Generate algebra problems with random integer values."""
    x = sp.Symbol('x')
    a, b = random.randint(-10, 10), random.randint(-10, 10)
    equation = sp.Eq(a*x + b, random.randint(-10, 10))
    solution = sp.solve(equation, x)[0]
    print("Solve for x:", equation)
    player_answer = float(input("Your answer: "))
    
    if player_answer == solution:
        print("Correct!")
    else:
        print(f"Incorrect! The correct answer is {solution}")

def projectile_game():
    """Adjust sliders to clear a wall with a projectile motion."""
    wall_x = random.randint(3, 7)
    wall_height = random.randint(5, 15)
    
    def plot_trajectory(a, b, c):
        x = np.linspace(0, 10, 100)
        y = a*x**2 + b*x + c
        
        plt.plot(x, y, label="Projectile Path")
        plt.axvline(wall_x, color='r', linestyle='--', label="Wall")
        plt.axhline(wall_height, color='g', linestyle='--', label="Wall Height")
        plt.ylim(0, max(y) + 5)
        plt.legend()
        plt.grid()
        plt.title("Projectile Game: Adjust to Clear the Wall")
        plt.show()
    
    interact(plot_trajectory, a=FloatSlider(-1, 1, 0.1), b=FloatSlider(0, 10, 0.5), c=FloatSlider(0, 5, 0.5))

# Run the games
scatter_plot_game()
algebra_practice_game()
projectile_game()
