num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
print("\nSelect an operation:")
print("1. Addition (+)")
print("2. Subtraction (-)")
print("3. Multiplication (*)")
print("4. Division (/)")
choice = input("Enter choice (1/2/3/4): ")
if choice == '1':
    result = num1 + num2
    operation = "+"
elif choice == '2':
    result = num1 - num2
    operation = "-"
elif choice == '3':
    result = num1 * num2
    operation = "*"
elif choice == '4':
    if num2 != 0:
        result = num1 / num2
        operation = "/"
    else:
        result = "Undefined (cannot divide by zero)"
        operation = "/"
else:
    result = "Invalid choice"
    operation = "?"
if isinstance(result, (int, float)):
    print(f"\nResult: {num1} {operation} {num2} = {result}")
else:
    print(f"\nError: {result}")
