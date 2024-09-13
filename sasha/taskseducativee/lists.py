def count_low_high(num_list):
  # Write your code here
    high = []
    low = []
    for i in num_list:
        if i > 50 or i % 3 == 0:
            high.append(i)
        else:
            low.append(i)
    return [len(low), len(high)]
print(count_low_high([20, 9, 51, 81, 50, 42, 77]))

