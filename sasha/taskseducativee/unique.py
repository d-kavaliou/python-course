def is_unique(input_str):
    result = ""
    for i in input_str:
        if i not in result:
            result = result + i
    if result == input_str:
        return True
    else:
        return False
  
print(is_unique('aad a v !'))
  
            
        