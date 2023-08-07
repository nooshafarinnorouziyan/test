import math 
a = float(input("enter a:"))
b = float(input("enter b:"))
c = float(input("enter c:"))
if a != 0:
   delta = b ** 2 - a * c
   if delta > 0 :
    x1=(-b + math.sqrt(delta))/2*a
    x2=(-b - math.sqrt(delta))/2*a
    print("result:/n x1 = {x1} /n = {x2}")
   
elif delta ==0:
 answer = -b/2*a 
 print(answer) 

elif delta <0:
  print("Error")

  
