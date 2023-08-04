import random
print("*** DICE ***")
print("if you bring 6 you are win and you have *prize* and roll again")
while True :
 
 dice =str(input("ROLL THE DICE"))
 if dice == 1 :
  result = 1
  break
 if dice == 2:
  result = 2
  break 
 if dice ==3:
  result = 3
  break
 if dice == 4 :
  result = 4
  break
 if dice == 5:
  result = 5 
 break
if dice == 6 :
 result = "*BRING 6 YOU ARE WIN ROLL AGAIN*"
