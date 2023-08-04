import random
print("this is a guessing game")
your_guess = int(input ("!!!!!enter your guess!!!!!:"))
random_number= random.randint(0,20)

count=1
while 1 :

 if your_guess==random_number:
      print("*****you are win*****") 
      break 
    
 elif your_guess > random_number:
        print("<<<<your guess is low>>>>")
count+=1

if your_guess < random_number:
        print("<<<<your guess is much>>>>")
count+=1

  
    