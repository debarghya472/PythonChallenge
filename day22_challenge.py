import random

num = random.randint(1,50)

print("try to guess a number between 1 to 50")

chances = 5

while True:
    if chances == 0:
        break
    print("Chances left: ",chances)
    n=int(input("enter your guess: "))
    if n == num:
        print("Correct guess:: No. of chances used = ",(6-chances))
        break
    chances=chances-1

if chances == 0:
    print("Better luck next time!")

