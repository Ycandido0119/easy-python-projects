def addition(num1, num2):
    return num1 + num2

def substraction(num1, num2):
    return num1 - num2

def multiplication(num1, num2):
    return num1 * num2

def division(num1, num2):
    if num2 == 0:
        return "Error! Division by zero."
    return num1 / num2

print("Welcome to the simple calculator!")
print("Select operation:")
print("1. Addition")
print("2. Subtraction")
print("3. Multiplication")
print("4. Division")

while True:
    choice = input("Enter choice (1/2/3/4): ")

    if choice in ['1', '2', '3', '4']:
        try:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))
        except ValueError:
            print("Invalid input. Please enter numeric values.")
            continue

        if choice == '1':
            print(num1, "+", num2, "=", addition(num1, num2))
        elif choice == '2':
            print(num1, "-", num2, "=", substraction(num1, num2))
        elif choice == '3':
            print(num1, "*", num2, "=", multiplication(num1, num2))
        elif choice == '4':
            print(num1, "/", num2, "=", division(num1, num2))
        next_calculation = input("Do you want to perform another calculation? (yes/no): ")
        if next_calculation.lower() != 'yes':
            print("Thank you for using the calculator. Goodbye!")
            break
    else:
        print("Invalid input. Please select a valid operation.")
    