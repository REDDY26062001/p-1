def fibonacci_series(n):
    fib_sequence = [0, 1]

    while fib_sequence[-1] + fib_sequence[-2] <= n:
        fib_sequence.append(fib_sequence[-1] + fib_sequence[-2])

    return fib_sequence

# Example: Print Fibonacci series until 100
n = int(input())
fibonacci_sequence = fibonacci_series(n)
print(f"Fibonacci Series until {n}: {fibonacci_sequence}")
