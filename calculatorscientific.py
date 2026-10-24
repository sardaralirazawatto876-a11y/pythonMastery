import math

def add(x, y): return x + y
def subtract(x, y): return x - y
def multiply(x, y): return x * y
def divide(x, y): return "Error! Division by zero." if y == 0 else x / y

def scientific_calculator():
    print("=== Scientific Python Calculator ===")
    print("Operations: 1:Add | 2:Sub | 3:Mul | 4:Div | 5:Sin | 6:Cos | 7:Tan | 8:Log | 9:Sqrt")
    
    while True:
        choice = input("\nEnter choice (1-9) or 'q' to quit: ")
        if choice.lower() == 'q':
            print("Goodbye!")
            break
            
        if choice in ('1', '2', '3', '4'):
            try:
                num1 = float(input("Enter first number: "))
                num2 = float(input("Enter second number: "))
                if choice == '1': print(f"Result: {add(num1, num2)}")
                elif choice == '2': print(f"Result: {subtract(num1, num2)}")
                elif choice == '3': print(f"Result: {multiply(num1, num2)}")
                elif choice == '4': print(f"Result: {divide(num1, num2)}")
            except ValueError:
                print("Invalid input. Use numbers only.")
        elif choice in ('5', '6', '7', '8', '9'):
            try:
                num = float(input("Enter number: "))
                if choice == '5': print(f"Result: {math.sin(math.radians(num))}")
                elif choice == '6': print(f"Result: {math.cos(math.radians(num))}")
                elif choice == '7': print(f"Result: {math.tan(math.radians(num))}")
                elif choice == '8': print(f"Result: {math.log10(num) if num > 0 else 'Error!'}")
                elif choice == '9': print(f"Result: {math.sqrt(num) if num >= 0 else 'Error!'}")
            except ValueError:
                print("Invalid input.")
        else:
            print("Invalid Choice.")

if __name__ == "__main__":
    scientific_calculator()
