"""
Task: Body Mass Index (BMI) Calculator

Objective:
Create a Python script that calculates the Body Mass Index (BMI) of a person, which is a value derived from the mass (weight) and height of an individual. The BMI is a useful measure to classify underweight, normal weight, overweight, and obese individuals.

Inputs:
    weight (float): The weight of the person in kilograms.
    height (float): The height of the person in meters.

Output:
    A string that contains the BMI value and the corresponding BMI category (Underweight, Normal weight, Overweight, Obese).

BMI Categories:
    - Underweight: BMI < 18.5
    - Normal weight: 18.5 ≤ BMI < 25
    - Overweight: 25 ≤ BMI < 30
    - Obese: BMI ≥ 30

Example:
    If a person weighs 70 kg and is 1.75 m tall, the BMI should be 22.86, which falls into the 'Normal weight' category.

Ensure the script handles invalid inputs gracefully and prompts the user to re-enter values if necessary.
"""

def calculate_bmi(weight, height):
    pass


# Simple assertions to test the calculate_bmi function
assert 'Underweight' in calculate_bmi(50, 1.8), "Test failed for Underweight category."
assert 'Normal weight' in calculate_bmi(70, 1.75), "Test failed for Normal weight category."
assert 'Overweight' in calculate_bmi(80, 1.7), "Test failed for Overweight category."
assert 'Obese' in calculate_bmi(100, 1.6), "Test failed for Obese category."

print("All tests passed!")
