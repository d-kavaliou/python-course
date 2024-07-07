# Exercise: String to Integer

def str_to_int(input_str):
    digits = []
    result = 0
    n = 1
    if input_str[0] == "-":
        is_negative = True
        input_str = input_str[1::]
    else:
        is_negative = False
    for d in input_str:
        digits.append(ord(d) - 48)
    for el in reversed(digits):
        result += el * n
        n *= 10
    if is_negative is True:
        result *= -1
    return result


s = '-5298'
print(str_to_int(s))
