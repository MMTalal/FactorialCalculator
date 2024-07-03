# Print explanation of factorial with an example
print("Factorial of a number:-\nIs the product of all positive integers less than or equal to this number\nFor example:\n5! = 5 × 4 × 3 × 2 × 1 = 120")

# Prompt the user to enter a number to calculate its factorial
number = int(input("Enter a number to calculate its factorial: "))

# Check if the entered number is less than zero
if number < 0:
    # Print an error message if the number is less than zero
    print(f"Your number {number} is less than zero, try again")
else:
    # Initialize the factorial variable
    factorial = 1
    
    # Use a for loop to calculate the factorial
    for i in range(1, number + 1):
        factorial *= i  # Multiply the current factorial value by i
        print(factorial)  # Print the current factorial value after each multiplication

    # Print the final result of the factorial
    print(f"The factorial of {number} is {factorial}.")
