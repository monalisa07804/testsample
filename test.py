try:
    # 1. Ask the user for a number
    number = int(input("Enter a number: "))
    
    # 2. Attempt a calculation
    result = 10 / number
    print(f"Success! 10 divided by {number} is {result}")

except ZeroDivisionError:
    # This runs if the user enters 0
    print("Error: You cannot divide by zero!")

except ValueError:
    # This runs if the user enters words or symbols instead of integers
    print("Error: Please enter a valid whole number!")
