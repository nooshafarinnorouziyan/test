
import random
print("this is a guessing game")

random_number= random.randint(1,20)
count=1

while count <= 5 :
    your_guess = int(input("!!!!!enter your guess!!!!!:"))

    if your_guess == random_number:
        print("*****you win*****") 
        break 
    
    elif your_guess < random_number:
        print("<<<<your guess is low>>>>")
        
    elif your_guess > random_number:
        print("<<<<your guess is much>>>>")
        
    count += 1

if count > 5:
    print("Sorry, you have exhausted your 5 guesses. The random number was:", random_number)
