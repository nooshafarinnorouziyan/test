print ("can we have triangle with these numbers")
side1 = float(input("enter the side 1:"))
side2 = float(input("enter the side 2:"))
side3 = float(input("enter the side 3:"))

max = max(side1 ,side2 , side3)

if max == side1:
     if side2+side3>max :
          print ("correct")
     else :
          print ("incorrect") 
elif max == side2: 
     if side1 + side3 > max :
          print("correct")
     else:
          print("incorrect")
else :
     if side2 + side1 > max :
          print("correct")
     else:
          print("incorrect")
