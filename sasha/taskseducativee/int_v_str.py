def str_to_int(input_str):
    input_str2 = input_str[::-1]
    res = dict()
    answ = 0
    if input_str2[-1] == '-':
        input_str2 = input_str2[0:-1]
    for i in range(len(input_str2)):
        res[i] = ord(input_str2[i]) - 48
    for i in res:
        answ += res[i]*(10**i) 
        i=i+1
    if input_str[0] == '-':
        return 0 - answ
    else:
        return (answ)


print(str_to_int('-1293'))