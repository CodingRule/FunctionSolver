import numpy as np
import matplotlib.pyplot as plt
import re
import mplcursors
from sympy import sympify, symbols

def calculate_formula(formula, x):
    """Calculates the value of a given formula at a given x."""
    x_symbol = symbols('x')
    formula_expr = sympify(formula)
    return formula_expr.subs(x_symbol, x)

def plot_graph(points, formula):
    """Plots a graph with points and a line."""
    x_values = [point[0] for point in points]
    y_values = [point[1] for point in points]
    
    plt.scatter(x_values, y_values, color='red', label='Points')
    
    x = np.linspace(min(x_values) - 10, max(x_values) + 10, 1000)  # Use a larger x range
    y = [calculate_formula(formula, val) for val in x]
    plt.plot(x, y, color='blue', label='Line')
    
    # Add the origin point
    plt.scatter(0, 0, color='green', label='Origin (0, 0)')
    
    # Make Ox and Oy lines more highlighted
    ax = plt.gca()
    ax.axhline(0, color='black', linewidth=1.5)
    ax.axvline(0, color='black', linewidth=1.5)
    
    for point in points:
        plt.annotate(point[2], (point[0], point[1]), textcoords="offset points", xytext=(0,10), ha='center')
    
    plt.xlabel('x')
    plt.ylabel('f(x)')
    plt.title('Graph of ' + formula)
    plt.legend()
    plt.grid(True)

    # Add annotations with coordinates on hover
    mplcursors.cursor(hover=True).connect("add", lambda sel: sel.annotation.set_text(f"({sel.target[0]:.2f}, {sel.target[1]:.2f})"))

    plt.show()

def main():
    formula = input('Enter a formula (e.g., "2 + 3*x"): ')
    points = []
    
    while True:
        point_name = input('Enter a point name (single uppercase letter) or "done" to finish: ')
        if point_name == 'done':
            break
        
        if len(point_name) == 1 and point_name.isupper():
            try:
                x = float(input('Enter x coordinate for point {}: '.format(point_name)))
                y = calculate_formula(formula, x)
                points.append((x, y, point_name))
                print('Point {}: ({}, {})'.format(point_name, x, y))
            except ValueError:
                print('Invalid input. Please enter a number.')
        else:
            print('Invalid point name. Please enter a single uppercase letter.')
    
    plot_graph(points, formula)

if __name__ == '__main__':
    main()
