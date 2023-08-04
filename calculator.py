import math 
print ("calculator program")
if op == "+":
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    result = num1 + num2

if op == "-":
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    result = num1 - num2

    if op == "*":
     num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    result = num1 * num2

if op == "/":
    num1 = int(input("enter num1:"))
    num2 = int(input("enter num2:"))
    if num2 == 0 :
     result = "Error"
else:
   result = num1 / num2


   if op == "sin":
      num1 = int(input("enter your number:"))
      result = math.sin(num1)

      if op == "tan":
         num1 =int(input("enter your number:"))
         result = math.tan(num1)

         if op == "cos":
            num1 = int(input("enter your number:"))
            result = math.cos(num1)

            if op == "cot":
               num1 = int(input("enter your number:"))
               n = math.tan(num1)

               if n == 0 :
                  result = "Error"
            else :
               result = 1 / math.tan(num1)
            if op == "factorial":
               num1 + int(input("enter your number:"))
               result = math.factorial

               if op == "sqrt":
                  num1 = int(input("enter your number:"))
                  result = math.sqrt

                  print (result)