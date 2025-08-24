import random

while True:
    user_input=input("Enter your choice[rock/paper/scissors]: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)

    print("You chose", user_input,", computer chose", computer_action)

    if user_input==computer_action:
        print("It's a tie!")
    elif user_input=="rock":
        if computer_action=="scissors":
            print("Rock smashes scissors! You win!")
        else:
            print("Paper covers rock! You lose.")
    elif user_input=="scissors":
        if computer_action=="paper":
            print("Scissors cuts paper! You win!")
        else:
            print("Rock smashes scissor! You lose.")
    elif user_input=="paper":
        if computer_action=="rock":
            print("Paper covers rock! You win!")
        else:
            print("Scissors cuts paper! You lose.")
    else:
        print("Invalid input!")
        play_again=input("Do you want to play again? (yes/no): ")
        if play_again!="yes":
            break
        
    