# Develop custom hash functions for both integers and strings to map inputs to a fixed range of output values. 
# Test these hash functions to ensure they distribute values evenly across the range.

def int_hash(x, num_buckets=100):
    pass


def string_hash(s, num_buckets=100):
    """ A simple hash function for strings. """
    hash_value = 0
    for char in s:
        # you can use the ord() function to get the ASCII value of a character
        pass

    return hash_value


def test_hash_distribution():
    num_buckets = 100
    int_buckets = [0] * num_buckets
    string_buckets = [0] * num_buckets
    test_integers = range(1, 1001)  # Testing with first 1000 positive integers
    test_strings = [f"key_{i}" for i in range(1, 1001)]  # Testing with 1000 simple strings

    # Test integer hash function
    for value in test_integers:
        bucket_index = int_hash(value, num_buckets)
        int_buckets[bucket_index] += 1

    # Test string hash function
    for value in test_strings:
        bucket_index = string_hash(value, num_buckets)
        string_buckets[bucket_index] += 1

    # Print the bucket usage to see the distribution for integers
    print("Integer Hash Distribution:")
    for i, count in enumerate(int_buckets):
        print(f"Bucket {i}: {count} hits")

    # Print the bucket usage to see the distribution for strings
    print("\nString Hash Distribution:")
    for i, count in enumerate(string_buckets):
        print(f"Bucket {i}: {count} hits")


# Run the hash distribution test
test_hash_distribution()
