import random
playing=True
x=str(random.randint(10,20))

print("I will think of a number between 10 and 20 and you have to guess the number one at a time.")
print("The game ends when you get 1 hero.")

while playing:
    guess=input("Give me your best shot: ")
    if x==guess:
        print("Yay! You won the game!")
        print("The number was ",x)
        break
    else:
        print("Not quite right, try again!")