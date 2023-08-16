import math 
print ("calculator program")
op = input("Enter operation (+, -, *, /, sin, cos, tan, cot, factorial, sqrt): ")

if op == "+":
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    result = num1 + num2

elif op == "-":
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    result = num1 - num2

elif op == "*":
     num1 = int(input("enter num1:"))
     num2 = int(input("enter num2:"))
     result = num1 * num2

elif op == "/":
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    if num2 == 0 :
     result = "Error"
    else:
       result = num1 / num2

elif op == "sin":
    num1 = int(input("enter your number (in radians):"))
    result = math.sin(num1)

elif op == "tan":
    num1 =int(input("enter your number (in radians):"))
    result = math.tan(num1)

elif op == "cos":
    num1 = int(input("enter your number (in radians):"))
    result = math.cos(num1)

elif op == "cot":
    num1 = int(input("enter your number (in radians):"))
    n = math.tan(num1)

    if n == 0 :
        result = "Error"
    else :
        result = 1 / math.tan(num1)

elif op == "factorial":
    num1 = int(input("enter your number:"))
    result = math.factorial(num1)

elif op == "sqrt":
    num1 = int(input("enter your number:"))
    result = math.sqrt(num1)

print (result)
