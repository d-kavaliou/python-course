import time

def memoize(f):
    cache = {}    
    return lambda *args: cache[args] if args in cache else cache.update({args: f(*args)}) or cache[args]


def fibonacci_naive(n):
    if n <= 1:
        return n
    return fibonacci_naive(n-1) + fibonacci_naive(n-2)

@memoize
def fibonacci_with_memoization(n):
    if n <= 1:
        return n
    return fibonacci_with_memoization(n-1) + fibonacci_with_memoization(n-2)


# Test without memoization (this will take a significant amount of time for large n)
start_time_naive = time.time()
print(f"Fibonacci(30) without memoization: {fibonacci_naive(40)}")
end_time_naive = time.time()
print(f"Execution time without memoization: {end_time_naive - start_time_naive:.4f} seconds")

# Test with memoization
start_time_memoized = time.time()
print(f"Fibonacci(30) with memoization: {fibonacci_with_memoization(100)}")
end_time_memoized = time.time()
print(f"Execution time with memoization: {end_time_memoized - start_time_memoized:.4f} seconds")