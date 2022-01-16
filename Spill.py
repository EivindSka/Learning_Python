
import time

print ("Welcome to my Quiz")

playing = input("Do you want to play a game? ")
score = 0


if playing.lower() != "yes":
    print ("Good Bye!")
    quit()

print ("Allright lets play!")

answer = input("What's the capital of Norway? \n")
if answer.lower() == "oslo":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")


answer = input("What is the main income to Norway? \n")
if answer == "oil and gas":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("Whats the capital of Sweden? \n")
if answer.lower() == "gothenburg":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

answer = input("What programming language was this made in? \n")
if answer.lower == "python":
    print ("Correct!")
    score += 1
else:
    print ("Incorrect!")

print("You got " + str(score) + " questions correct!")
print("You got " + str((score / 4)*100) + "%!")

