def convert_temperature(temp_input):
    """
    Convert a temperature from Fahrenheit to Celsius or vice versa.

    The function takes a string that consists of a number followed by 
    a single character, 'C' or 'F', representing Celsius or Fahrenheit, respectively.
    It returns the temperature converted to the other unit, as a string formatted like the input.

    The conversion formulas are as follows:
    - Celsius to Fahrenheit: (C * 9/5) + 32
    - Fahrenheit to Celsius: (F - 32) * 5/9

    For example:
    - "100C" should return "212F"
    - "32F" should return "0C"
    """
    pass


# Assertions to test the convert_temperature function
assert convert_temperature('100C') == '212F', "Test failed for '100C'. Expected: '212F'"
assert convert_temperature('32F') == '0C', "Test failed for '32F'. Expected: '0C'"
assert convert_temperature('0C') == '32F', "Test failed for '0C'. Expected: '32F'"
assert convert_temperature('-40C') == '-40F', "Test failed for '-40C'. Expected: '-40F'"
assert convert_temperature('212F') == '100C', "Test failed for '212F'. Expected: '100C'"

print("All tests passed!")
