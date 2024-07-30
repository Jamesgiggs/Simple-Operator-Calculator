# Functions for basic arithmetic operations
def add(x, y):
    return x + y


def subtract(x, y):
    return x - y


def multiply(x, y):
    return x * y


def divide(x, y):
    if y == 0:
        return "Error! Division by zero."
    return x / y


def exponent(x, y):
    return x ** y


def modulo(x, y):
    return x % y


# Function to display the menu
def print_menu():
    print("Select operation:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exponent")
    print("6. Modulo")
    print("7. Exit")


def main():
    while True:
        print_menu()
        choice = input("Enter choice (1/2/3/4/5/6/7): ")

        if choice == '7':
            print("Exiting the calculator. Goodbye!")
            break

        if choice in ['1', '2', '3', '4', '5', '6']:
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
            except ValueError:
                print("Invalid input! Please enter a number.")
                continue

            if choice == '1':
                print(f"The result is: {add(num1, num2)}")
            elif choice == '2':
                print(f"The result is: {subtract(num1, num2)}")
            elif choice == '3':
                print(f"The result is: {multiply(num1, num2)}")
            elif choice == '4':
                print(f"The result is: {divide(num1, num2)}")
            elif choice == '5':
                print(f"The result is: {exponent(num1, num2)}")
            elif choice == '6':
                print(f"The result is: {modulo(num1, num2)}")
        else:
            print("Invalid input! Please select a valid option.")


if __name__ == "__main__":
    main()
