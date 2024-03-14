def check_even_odd(num):
    """Check if a number is even or odd."""
    if num % 2 == 0:
        return "Even"
    else:
        return "Odd"

# Get user input
num = int(input("Enter a number: "))

# Check and print result
result = check_even_odd(num)
print(f"{num} is {result}.")