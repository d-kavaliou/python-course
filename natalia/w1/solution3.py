def calculate_bmi(weight, height):
    bmi = weight / height ** 2
    if bmi < 18.5:
        category = 'Underweight'
    elif 18.5 <= bmi < 25:
        category = 'Normal weight'
    elif 25 <= bmi < 30:
        category = 'Overweight'
    elif bmi >= 30:
        category = 'Obese'
    return category

# Simple assertions to test the calculate_bmi function
assert 'Underweight' in calculate_bmi(50, 1.8), "Test failed for Underweight category."
assert 'Normal weight' in calculate_bmi(70, 1.75), "Test failed for Normal weight category."
assert 'Overweight' in calculate_bmi(80, 1.7), "Test failed for Overweight category."
assert 'Obese' in calculate_bmi(100, 1.6), "Test failed for Obese category."

print("All tests passed!")