import random 
print ("///the random list///")
number_ed=int(input("how many number are in the list???"))
num_list =[]
while len (num_list) < number_ed:
    number = random.randint(1,number_ed+10)
if number not in num_list:
    num_list.append(number)
    result = num_list
    print("your list is complete")