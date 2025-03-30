from calculator import add, subtract, multiply, divide, power

def main():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Power")
    
    choice = input("Enter choice (1/2/3/4/5): ")

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))
    
    if choice == '1':
        print("Result:", add(num1, num2))
    elif choice == '2':
        print("Result:", subtract(num1, num2))
    elif choice == '3':
        print("Result:", multiply(num1, num2))
    elif choice == '4':
        print("Result:", divide(num1, num2))
    elif choice == '5':
        try:
            print("Result:", power(num1, num2))
        except ValueError as e:
            print(e)
    else:
        print("Invalid choice")

if __name__ == "__main__":
    main()