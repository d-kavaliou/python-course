class Stack():
    def __init__(self):
        self.items = []

    def push(self, item):
        self.items.append(item)				

    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []
    
    def peek(self):
        if not self.is_empty():
            return self.items[-1]
        
    def get_stack(self):
        return self.items
    

def convert_num_to_bin(dec_num):

    stack = Stack()

    if dec_num == 0:
        return 0

    while dec_num != 0:
        stack.push(str(dec_num % 2))
        dec_num = dec_num //2

    rev_str = ""
    
    while not stack.is_empty():
        rev_str += stack.pop()
    
    return rev_str


print(convert_num_to_bin(83))
print(convert_num_to_bin(213))
print(convert_num_to_bin(0))




