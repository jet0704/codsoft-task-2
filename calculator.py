class Calculator:
    def add(self, a, b):
        return a + b

    def subtract(self, a, b):
        return a - b

    def multiply(self, a, b):
        return a * b

    def divide(self, a, b):
        if b == 0:
            return "Error! Division by zero is not allowed."
        else:
            return a / b


calc = Calculator()

while True:
    print("\n1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")

    choice = input("Enter the number of your choice: ")

    if choice == '1':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The sum of {num1} and {num2} is {calc.add(num1, num2)}")

    elif choice == '2':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The difference of {num1} and {num2} is {calc.subtract(num1, num2)}")

    elif choice == '3':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The product of {num1} and {num2} is {calc.multiply(num1, num2)}")

    elif choice == '4':
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number: "))
        print(f"The quotient of {num1} and {num2} is {calc.divide(num1, num2)}")

    elif choice == '5':
        print("Exiting the calculator.")
        break

    else:
        print("Invalid input! Please enter a number between 1 and 5.")