print("Can we have a triangle with these numbers?")
side1 = float(input("Enter side 1: "))
side2 = float(input("Enter side 2: "))
side3 = float(input("Enter side 3: "))

sides = [side1, side2, side3]
sides.sort(reverse=True)

largest_side = sides[0]

if sides[1] + sides[2] > largest_side:
    print("Yes, the sides can form a triangle.")
else:
    print("No, the sides cannot form a triangle.")
     
