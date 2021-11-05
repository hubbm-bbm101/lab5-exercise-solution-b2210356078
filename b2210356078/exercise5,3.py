import random
number = random.randint(1,101)
x = int(input("Please enter a integer: "))
while x != number:
    while x < number:
        print("The number that you pick is smaller than the number that you trying the find")
        x = int(input("Please enter a higher number:"))
    while x > number:
        print("The number that you pick is bigger than the number that you trying the find")
        x = int(input("Please enter a lower number:"))
print("You guessed right :*>")