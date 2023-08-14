import random

score = 0

while score < 6:
    roll = random.randint(1, 6)
    print("You rolled a", roll)
    if roll == 6:
        print("Congratulations! You get to roll again.")
    else:
        score += roll
        print("Your score is now", score)

print("Final score:", score)
print("You win!")