import random

user_wins = 0
computer_wins = 0
ties = 0

rock_paper_scissor_list = ["rock","paper","scissor"]
while True :
    user_input = input("type rock/paper/scissor or q to quit:- ").lower()

    if user_input == "q":
        break
    elif user_input not in rock_paper_scissor_list:
        print("opps you can only type what is asked")
        continue
    random_number = random.randint(0,2)
    computer_guess = rock_paper_scissor_list[random_number] 
    if user_input == "rock" :
        if computer_guess =="rock":
            print("Tie")
            ties += 1
        elif computer_guess == "paper":
            print("computer wins")
            computer_wins += 1
        elif computer_guess == "scissor":
            print("you win")
            user_wins += 1

    if user_input == "paper" :
        if computer_guess =="rock":
            print("user win")
            user_wins += 1
        elif computer_guess == "paper":
            print("tie")
            ties += 1
        elif computer_guess == "scissor":
            print("computer win")
            computer_wins += 1

    if user_input == "scissor" :
        if computer_guess =="rock":
            print("computer win")
            computer_wins += 1
        elif computer_guess == "paper":
            print("user win")
            user_wins += 1
        elif computer_guess == "scissor":
            print("tie")
            ties += 1

print("you wins", user_wins, "times")
print("computer wins" , computer_wins, "times")
print("tie happen" ,ties , "times")

print("Good byeeee!! ladla")




