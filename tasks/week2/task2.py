# Try to guess Time Complexity of the following functions

# Function 1
def get_first_element(arr):
    return arr[0]  # Accessing the first element is constant time O(1)


# Example usage:
array = [5, 4, 3, 2, 1]
print(get_first_element(array))


# Function 2
def sum_elements(arr):
    total = 0
    for element in arr:
        total += element  # Sum each element, one at a time
    return total


# Example usage:
array = [5, 4, 3, 2, 1]
print(sum_elements(array))


# Function 3
def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]  # Swap if elements are in wrong order
    return arr


# Example usage:
array = [5, 3, 8, 6, 2]
print(bubble_sort(array))
