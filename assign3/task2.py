import math

# Ask the user to enter a number
number = float(input("Enter a number: "))

if number > 0:
    # Calculate and display the square root
    print("Square root:", math.sqrt(number))
    
    # Calculate and display the logarithm
    print("Logarithm:", math.log(number))
    
    # Calculate and display the sine
    print("Sine:", math.sin(number))
else:
    print("Please enter a number greater than 0.")

