# Define a function to calculate factorial
def factorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

# Get user input and calculate the factorial
number = int(input("Enter a number: "))
print(f"The factorial of {number} is: {factorial(number)}")
