from stack import Stack

# solution 1

def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        n = dec_num % 2
        s.push(n)
        dec_num //= 2
    bin_num = 0
    while not s.is_empty():
        bin_num *= 10
        bin_num += s.pop()
    return bin_num  # int

print(convert_int_to_bin(3))
print(convert_int_to_bin(23))

# solution 2

def convert_int_to_bin(dec_num):
    s = Stack()
    while dec_num > 0:
        n = dec_num % 2
        s.push(str(n))
        dec_num //= 2
    bin_num = ''
    while not s.is_empty():
        bin_num += s.pop()
    return bin_num  # str

print(convert_int_to_bin(3))
print(convert_int_to_bin(11))

# educative solution

# def convert_int_to_bin(dec_num):
    
#     if dec_num == 0:
#         return 0
    
#     s = Stack()

#     while dec_num > 0:
#         remainder = dec_num % 2
#         s.push(remainder)
#         dec_num = dec_num // 2

#     bin_num = ""
#     while not s.is_empty():
#         bin_num += str(s.pop())

#     return bin_num

# print(convert_int_to_bin(56))
# print(convert_int_to_bin(2))
# print(convert_int_to_bin(32))
# print(convert_int_to_bin(10))

# print(int(convert_int_to_bin(56),2)==56)