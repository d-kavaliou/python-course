def convert_temperature(temp_input):
    if temp_input[-1] == 'F':
        temp = f'{(int(temp_input[:-1]) - 32) *  5 // 9}C'
    else:
        temp = f'{(int(temp_input[:-1]) * 9 // 5) + 32}F'
    return temp


# Assertions to test the convert_temperature function
assert convert_temperature('100C') == '212F', "Test failed for '100C'. Expected: '212F'"
assert convert_temperature('32F') == '0C', "Test failed for '32F'. Expected: '0C'"
assert convert_temperature('0C') == '32F', "Test failed for '0C'. Expected: '32F'"
assert convert_temperature('-40C') == '-40F', "Test failed for '-40C'. Expected: '-40F'"
assert convert_temperature('212F') == '100C', "Test failed for '212F'. Expected: '100C'"

print("All tests passed!")