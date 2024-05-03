
def calculate_result(x, y):
    result = 3*x+5*y
    return result

assert calculate_result(3, 4) == 29, "Test failed for inputs (3, 4)"
assert calculate_result(0, 0) == 0, "Test failed for inputs (0, 0)"
assert calculate_result(-1, -2) == -13, "Test failed for inputs (-1, -2)"
assert calculate_result(5, 5) == 40, "Test failed for inputs (5, 5)"
assert calculate_result(1, 1) == 8, "Test failed for inputs (1, 1)"

print("All tests passed!")