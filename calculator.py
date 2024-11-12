# Function to perform basic arithmetic operations
def calculator():
    # Get user input for two numbers and an operator
    try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        # Perform the calculation based on the operation
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 != 0:
                result = num1 / num2
            else:
                result = "Error! Division by zero."
        else:
            result = "Invalid operator!"

        # Print the result
        print(f"{num1} {operation} {num2} = {result}")
    except ValueError:
        print("Invalid input! Please enter numeric values.") 
