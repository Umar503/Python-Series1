def generate_fibonacci(n):
    fibonacci_sequence = []
    
    # First two terms of the Fibonacci sequence
    a, b = 0, 1
    
    # Generate Fibonacci sequence up to n terms
    for _ in range(n):
        fibonacci_sequence.append(a)
        a, b = b, a + b
    
    return fibonacci_sequence

# Get user input for the number of terms
num_terms = int(input("Enter the number of terms for the Fibonacci sequence: "))

# Check if the input is a positive integer
if num_terms <= 0:
    print("Please enter a positive integer.")
else:
    # Generate and print the Fibonacci sequence
    fibonacci_result = generate_fibonacci(num_terms)
    print(f"The Fibonacci sequence up to {num_terms} terms is: {fibonacci_result}")
