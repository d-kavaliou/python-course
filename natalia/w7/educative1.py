# Exercise: From List to Tuple

my_list = [34, 82.6, "Darth Vader", 17, "Hannibal"]
my_tuple = (my_list[0], my_list[-1], len(my_list))
print(my_tuple)

# Exercise: Kth Maximum Integer in a List

test_list = [40, 35, 82, 14, 22, 66, 53]
k = 2
test_list.sort(reverse=True)
ind = k - 1
kth_max = test_list[ind]
print(test_list) # sorted
print(kth_max)

# Exercise: Highs and Lows

def count_low_high(num_list):
    high_list = [n for n in num_list if n > 50 or n % 3 == 0]
    low_list = [m for m in num_list if m not in high_list]
    return [len(high_list), len(low_list)]

num_list = [20, 9, 51, 81, 50, 42, 77]
print(count_low_high(num_list))