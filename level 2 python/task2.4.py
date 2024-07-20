def generate_fibonacci_sequence(n):
    fibonacci_sequence = [0, 1]
    while len(fibonacci_sequence) < n:
        fibonacci_sequence.append(fibonacci_sequence[-1] + fibonacci_sequence[-2])
    return fibonacci_sequence[:n]

n = int(input("Enter the number of terms for the Fibonacci sequence: "))
fibonacci_sequence = generate_fibonacci_sequence(n)
print(f"Fibonacci sequence up to {n} terms: {fibonacci_sequence}")
