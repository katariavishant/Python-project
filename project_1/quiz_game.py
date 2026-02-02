print("Welcome to the Quiz Game!")
user_concent = input("Do you wanna play ? ")

if user_concent.lower() != "yes":
    print("Go to hell nard!")
    quit()

score = 0

answer = input("is modi alive? ")
if answer.lower() == "yes":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("Full form of CPU? ")
if answer.lower() == "central processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")


answer = input("Full form of GPU? ")
if answer.lower() == "graphics processing unit":
    print("correct!")
    score += 1
else:
    print("incorrect!")

print("you did well!")
print("your score is " + str(score))

