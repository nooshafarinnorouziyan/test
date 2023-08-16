name = input("Enter the name:")
family = input("Enter the family:")
num1 = int(input("Enter the chemistry score:"))
num2 = int(input("Enter the math score:"))
num3 = int(input("Enter the physics score:"))
so = num1 + num2 + num3
avrage = so / 3

if avrage < 12:
    print("Fail")
    
elif 12 <= avrage < 17:
    print ("Normal")
    
else:
    print ("Great")
    
print("Your name is", name, family, "and your average score is", avrage)

