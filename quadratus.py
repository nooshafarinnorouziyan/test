import math 

a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))

if a != 0:
   delta = b ** 2 - 4 * a * c  # Fix: delta formula should be b**2 - 4ac
   if delta > 0 :
       x1 = (-b + math.sqrt(delta)) / (2*a)  # Fix: Add parentheses in denominator
       x2 = (-b - math.sqrt(delta)) / (2*a)  # Fix: Add parentheses in denominator
       print(f"Result:\n x1 = {x1}\n x2 = {x2}")  # Fix: Use f-string to print results
   
   elif delta == 0:  # Fix: should use elif here
       answer = -b / (2*a)  # Fix: Add parentheses in denominator
       print(answer) 

   else:  # Fix: No need for another if statement, just use else
       print("Error")
else:
    print("Error: a cannot be zero")  # Fix: add error message if a is zero
  
