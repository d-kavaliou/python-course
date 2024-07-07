# Exercise: Is Unique

def is_unique(input_str):
    d = dict()
    for symb in input_str:
        if symb in d:
            d[symb] += 1
        else:
            d[symb] = 1
    return all(value == 1 for value in d.values())

print(is_unique(''))