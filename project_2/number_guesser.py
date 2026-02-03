import random

top_of_range = input("enter the top of the range starts with 0:- ")

if top_of_range.isdigit():
    top_of_range = int(top_of_range)

    if top_of_range <= 0:
        print("specify a positive top of range")

else:
    print("specify a number for top of range")


random_number = random.randint(0, top_of_range)
count = 0
while True :
    count += 1
    guess = input("write your guess ")

    if guess.isdigit():
        guess = int(guess)

        if guess < 0:
            print("write a positive guess")
            continue

    else:
        print("write a number as guess")
        continue

    if guess == random_number :
        print("boyaaa! you win")
        break

    elif guess<random_number:
        print("guess is below the answer")
        
        continue
    else:
        print("guess is above the answer")
        
        continue


print("you got it in", count , "tries!!" )
