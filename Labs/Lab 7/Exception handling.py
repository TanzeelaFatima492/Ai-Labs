try:
    a = int(input("Num1: ")); b = int(input("Num2: "))
    print(a / b)
except ZeroDivisionError: print("Cannot divide by zero")
except ValueError: print("Invalid input")
