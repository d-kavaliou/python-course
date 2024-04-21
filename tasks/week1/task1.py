"""
Task: Linear Equation Calculator

The objective of this task is to write a Python function that calculates a result based on the linear equation: result = 3x + 5y.

Inputs:
    x (int): An integer representing the 'x' variable in the equation.
    y (int): An integer representing the 'y' variable in the equation.

Output:
    An integer result calculated using the given linear equation.

Example:
    If x is 3 and y is 4, the function should return 29, since 3*3 + 5*4 = 29.

The function should be accompanied by unit tests that verify its correctness for various inputs.
"""


def calculate_result(x, y):
    pass


# Assertions to test the calculate_result function
assert calculate_result(3, 4) == 29, "Test failed for inputs (3, 4)"
assert calculate_result(0, 0) == 0, "Test failed for inputs (0, 0)"
assert calculate_result(-1, -2) == -13, "Test failed for inputs (-1, -2)"
assert calculate_result(5, 5) == 40, "Test failed for inputs (5, 5)"
assert calculate_result(1, 1) == 8, "Test failed for inputs (1, 1)"

print("All tests passed!")