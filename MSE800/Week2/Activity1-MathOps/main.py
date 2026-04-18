import math

#instructions
def show_instrcutions():
    print("==== Math Calculator ====")
    print("Use operators like +  -  *  /  %  ! (factorial)")
    print("Supports integers, floats, and complex numbers (e.g., 1+5j)")
    print("\n")

#Parse input
def parse_input(value):
    try:
        if "." in value:
            return float(value)
        elif "j" in value:
            return complex(value)
        else:
            return int(value)
    except:
        return None

#Basic math Ops
def basic_ops(a, b, operator):
    try:
        if operator == "+":
            return a + b
        elif operator == "-":
            return a - b
        elif operator == "*":
            return a * b
        elif operator == "/":
            return a / b
        elif operator == "%":    
            return a % b
        else:
            return "Invalid Operator"
    except Exception as e:
        return f"Error: {e}"

#factorial 
def factorial(n):
    try:
        if isinstance(n, complex):
            return "Factorial not supported on complex numbers"
        return math.factorial(n)
    except Exception as e:
        return f"Error: {e}"

def main():
    show_instrcutions()

    operator = input("Enter Operator: ")
    if operator == "!":
        factorialNum = parse_input(input("Enter Number: "))
        if factorialNum is None:
            print("Invalid Input")
        else: 
            print("Result: ", factorial(factorialNum))
    else:
        num1 = parse_input(input("Enter first number: "))
        num2 = parse_input(input("Enter second number: "))

        if num1 is None or num2 is None:
            print("Invalid Input")
        else: 
            print("Result: ", basic_ops(num1, num2, operator))

if __name__ == "__main__":
    main()



